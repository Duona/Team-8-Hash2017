import numpy as np
from collections import namedtuple

# purpose of this code is to read data and put it into convenient data structures

Endpoint = namedtuple('Endpoint', 'latency requests')
Cache = namedtuple('Cache', 'endpoints')


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
            # endpoints{id} = latency, dict of requests {vidID} = nOrequests
            endpoints[curEndpoint] = (Endpoint(eLatency, {}))
            for j in range(nmOcaches):
                c = f.readline().strip().split(" ")
                cacheId = int(c[0])
                cLatency = int(c[1])
                # caches{id} = endpoints{eId} = cLatency
                caches[cacheId] = caches.get(cacheId, Cache({}))
                caches[cacheId].endpoints[curEndpoint] = cLatency

        for line in f:
            request = line.strip().split(" ")
            video = int(request[0])
            ep = int(request[1])
            nmOrequests = int(request[2])

            # ensures that a single video is requested once per endpoint. THIS TRICKY REQUEST INPUT
            endpoints[ep].requests[video] = endpoints[ep].requests.get(video, 0)
            endpoints[ep].requests[video] += nmOrequests

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
            # checks if the video can be added to the cache
            if vid_sizes[vid] <= capacity:
                # iterates through each endpoint connected to the cache
                for e in caches[cache].endpoints:
                    # checks if video is requested by the endpoint
                    if vid in endpoints[e].requests:
                        table[vid][cache] += (endpoints[e].latency - caches[cache].endpoints[e]) * \
                                             endpoints[e].requests[vid]
    return table
