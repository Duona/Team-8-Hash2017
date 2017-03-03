import numpy as np
from collections import namedtuple

#purpose of this code is to read data and put it into convenient data structures


Request = namedtuple('Request', 'idNo endpointID nmOrequests')
Endpoint = namedtuple('Endpoint', 'idNo latency requests')
Cache = namedtuple('Cache', 'idNo latency endpoint cur_cap')
#classes aren't needed. cool...

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
        endpoints = []
        caches = [[] for i in xrange(infos[3])]




        for i in xrange(infos[1]):
            endpoint = f.readline().strip().split(" ")
            endpoints.append(Endpoint(len(endpoints), int(endpoint[0]), set([])))
            for j in range(int(endpoint[1])):
                cache = f.readline().strip().split(" ")
                caches[int(cache[0])].append(Cache(int(cache[0]), int(cache[1]), len(endpoints) - 1, capacity))
        for line in f:
            request = line.strip().split(" ")
            endpoints[int(request[1])].requests.update(Request(int(request[0]), int(request[1]), int(request[2])))
    return infos, vid_sizes, endpoints, caches


# temp = read_data('example.in')
# for i in range(len(temp[2])):
#     print temp[2][i].idNo, temp[2][i].latency
#     for j in temp[2][i].requests:
#         print j.idNo, j.endpointID, j.nmOrequests, '|',
#     print
#
# for i in temp[3]:
#     for j in i:
#         print j.idNo, j.latency, j.endpoint, '|',
#     print

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
            for c in caches[cache]:
                #checks if video is requested by the endpoint
                if vid in endpoints[c.endpoint].requests:
                #for r in endpoints[c.endpoint].requests:
                    #if vid == r.idNo: #GET THIS TO BE EFFICIENT
                        # might not be needed
                        # checks if the video can be added to the cache
                        if vid_sizes[vid] <= capacity:
                            table[vid][cache] += (endpoints[c.endpoint].latency - c.latency) #* endpoints[c.endpoint].requests[vid].nmOrequests
                        #break
                        #set DON'T support convenient way to retrieve videos
    return table


