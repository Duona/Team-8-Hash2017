import numpy as np
from collections import namedtuple

# purpose of this code is to read data and put it into convenient data structures

# DATA_PROCESS2 difference: maps caches to relevant videos to the cache for faster table computation
# turns out it's more efficient
Endpoint = namedtuple('Endpoint', 'latency requests caches')
Cache = namedtuple('Cache', 'endpoints videos')


# Gets data
def read_data(file_name):
    with open(file_name) as f:
        # nmOvideos, nmOendpoints, nmOrequest, nmOcaches, capacity
        infos = f.readline().strip().split(" ")
        for i in range(len(infos)):
            infos[i] = int(infos[i])

        nmOvideos = infos[0]
        nmOendpoints = infos[1]
        nmOrequest = infos[2]
        nmOcaches = infos[3]
        capacity = infos[4]

        # reads video sizes
        vid_sizes = f.readline().strip().split(" ")
        for i in range(len(vid_sizes)):
            vid_sizes[i] = int(vid_sizes[i])

        endpoints = {}
        caches = {}

        # processes endpoint -> caches part of the file
        for i in xrange(nmOendpoints):
            ep = f.readline().strip().split(" ")
            eLatency = int(ep[0])
            nmOcaches = int(ep[1])
            curEndpoint = len(endpoints)
            # endpoints{id} = latency, dict of requests {vidID} = nOrequests, set of caches connected to
            endpoints[curEndpoint] = (Endpoint(eLatency, {}, set()))  # sets are ok
            for j in range(nmOcaches):
                c = f.readline().strip().split(" ")
                cacheId = int(c[0])
                cLatency = int(c[1])
                # caches{id} = endpoints{eId} = cLatency, videos{vidId} = set of eId which requests vidId
                caches[cacheId] = caches.get(cacheId, Cache({}, {}))
                caches[cacheId].endpoints[curEndpoint] = cLatency
                # forms a set of caches which endpoint is connected to
                endpoints[curEndpoint].caches.add(cacheId)

        for line in f:
            request = line.strip().split(" ")
            video = int(request[0])
            ep = int(request[1])
            nmOrequests = int(request[2])

            # ensures that a single video is requested once per endpoint. THIS IS BECAUSE OF TRICKY REQUEST INPUT
            endpoints[ep].requests[video] = endpoints[ep].requests.get(video, 0)
            endpoints[ep].requests[video] += nmOrequests

            # adds video to cache if it's being requested by the endpoint cache is connected to
            for c in endpoints[ep].caches:
                # uses set in case same video is requested by several endpoints connected to a single cache
                caches[c].videos[video] = caches[c].videos.get(video, set())
                caches[c].videos[video].add(ep)

    return infos, vid_sizes, endpoints, caches


# Constructs an NmOfVideos X NmOfCaches array where an i,j position
# represnts time which would be saved if i'th video would be put in j'th cache
def process_data(data):
    infos, vid_sizes, endpoints, caches = data
    nmOvideos = infos[0]
    nmOendpoints = infos[1]
    nmOrequest = infos[2]
    nmOcaches = infos[3]
    capacity = infos[4]

    table = np.zeros(nmOvideos * nmOcaches).reshape(nmOvideos, nmOcaches)

    for cache in xrange(nmOcaches):
        for vid in xrange(nmOvideos):
            # if video is relevant to current cache and fits in it
            if vid in caches[cache].videos and vid_sizes[vid] <= capacity:
                # loops through every connected endpoint to the current cache and calculates time saved
                for e in caches[cache].videos[vid]:
                    table[vid][cache] += (endpoints[e].latency - caches[cache].endpoints[e]) * \
                                         endpoints[e].requests[vid]
    return table
