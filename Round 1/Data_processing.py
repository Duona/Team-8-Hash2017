import numpy as np
from collections import namedtuple

#purpose of this code is to read data and put it into convenient data structures


Request = namedtuple('Request', 'endpointID nmOrequests')
Endpoint = namedtuple('Endpoint', 'latency requests')
Cache = namedtuple('Cache', 'endpoints videos')


#Gets data
def read_data(file_name):
    with open(file_name) as f:
        #nmOvideos, nmOendpoints, nmOrequest, nmOcaches, capacity
        infos = f.readline().strip().split(" ")
        for i in range(len(infos)):
            infos[i] = int(infos[i])
        capacity = infos[4]
        vid_sizes = f.readline().strip().split(" ")
        for i in range(len(vid_sizes)):
            vid_sizes[i] = int(vid_sizes[i])
        endpoints = {}
        caches = {}

        #endpoints{id} = latency, dict of requests
        #caches{id} = endpoints{eId} = cLatency, videos{vidId} = eId


        for i in xrange(infos[1]):
            endpoint = f.readline().strip().split(" ")
            eLatency = int(endpoint[0])
            nmOcaches = int(endpoint[1])
            curEndpoint = len(endpoints)
            endpoints[curEndpoint] = (Endpoint(eLatency, {} ))
            for j in range(nmOcaches):
                cache = f.readline().strip().split(" ")
                cacheId = int(cache[0])
                cLatency = int(cache[1])
                caches[cacheId] = caches.get(cacheId, Cache({}, {}))
                caches[cacheId].endpoints[curEndpoint] = cLatency

        for line in f:
            request = line.strip().split(" ")
            video = int(request[0])
            endpoint = int(request[1])
            nmOrequests = int(request[2])

            endpoints[endpoint].requests[video] = nmOrequests

            # for c in caches:
            #     if c in endpoints[endpoint]:
            #         caches[c].videos[video] =
    return infos, vid_sizes, endpoints, caches



#Constructs an NmOfVideos X NmOfCaches array where an i,j position
#represnts time which would be saved if i'th video would be put in j'th cache
def process_data(data):
    infos, vid_sizes, endpoints, caches = data
    nmOvideos = infos[0]
    nmOendpoints = infos[1]
    nmOrequest = infos[2]
    nmOcaches = infos[3]
    capacity = infos[4]



    table = np.zeros(nmOvideos*nmOcaches).reshape(nmOvideos, nmOcaches)
    #VERY VERY INEFFICIENT
    #interates through every possible combination of video in cache
    for cache in xrange(nmOcaches):
        for vid in xrange(nmOvideos):
            #iterates through each endpoint connected to the cache
            for c in caches[cache].endpoints:
                #checks if video is requested by the endpoint
                if vid in endpoints[c].requests:
                #for r in endpoints[c.endpoint].requests:
                    #if vid == r.idNo: #GET THIS TO BE EFFICIENT
                        # might not be needed
                        # checks if the video can be added to the cache
                        if vid_sizes[vid] <= capacity:
                            table[vid][cache] += (endpoints[c].latency - caches[cache].endpoints[c]) * endpoints[c].requests[vid]
                        #break
                        #set DON'T support convenient way to retrieve videos
    return table

# data = read_data('kittens.in')
# print data[3]
# print process_data(data)

