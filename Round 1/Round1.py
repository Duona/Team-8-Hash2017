def read_data(file_name):
    with open(file_name) as f:
        infos = f.readline().strip().split(" ")
        for i in range(len(infos)):
            infos[i] = int(infos[i])
        capacity = infos[4]
        videos = f.readline().strip().split(" ")
        for i in range(len(videos)):
            videos[i] = int(videos[i])
        endpoints = []
        caches = {}
        requests = [-1] * infos[0]

        # endpoints[[latency, [cacheIds, ...]]] latency for i'th endpoint
        # caches:{chace_id: [[endpoint_id, latency, current_capacity], ...]}
        # requests[[video_id, endpoint, no_of_requests]] for i'th video


        for i in xrange(infos[1]):
            endpoint = f.readline().strip().split(" ")
            endpoints.append([int(endpoint[0]), []])
            for i in range(int(endpoint[1])):
                cache = f.readline().strip().split(" ")
                if caches.get(cache[0]) == None:
                    caches[cache[0]] = []
                if cache[0] not in endpoints[len(endpoints) - 1][1]:
                    endpoints[len(endpoints) - 1][1].append(cache[0])
                caches[cache[0]].append([len(endpoints) - 1, int(cache[1]), capacity])
        for line in f:
            request = line.strip().split(" ")
            requests[int(request[0])] = [int(request[0]), int(request[1]), int(request[2])]
        for i in xrange(len(requests)):
            if requests[i] == -1:
                requests[i] = [i, -1, 0]

    return infos, videos, endpoints, caches, requests


data = read_data('kittens.in')

#print data[2]

infos = data[0]
num_of_videos = infos[0]
capacity = infos[4]


size_of_videos = data[1]
endpoints = data[2]
caches = data[3]
requests = data[4]


# Find 'heaviest' videos in terms of latency
weighted_videos = [-1]*num_of_videos



for request in requests:
    # add weight: amount * central server latency
    weight = request[2] * endpoints[request[1]][0]
    weighted_videos[request[0]]=(request[0], weight)

for i in xrange(len(weighted_videos)):
    if weighted_videos[i] == -1:
        weighted_videos[i] = (i, 0)

# Sort by calculated weight
weighted_videos.sort(key=lambda tup: tup[1], reverse=True)

#print weighted_videos

video_to_cache = []

# iterate all videos
for video in weighted_videos:

    # list requests for video
    video_requests = []
    for request in requests:
        if request[0] == video[0]:
            video_requests.append(request)

    # Find ideal cache
    weighted_caches = []
    for cache in caches:
        cache_weight = 0
        for request in video_requests:

            for connection in caches[cache]:
                if connection[0] == request[1]:
                    # Cache latency of endpoint * amount of request
                    cache_weight += connection[1] * request[2]
            weighted_caches.append((cache, cache_weight))

    #make a check if cache is able to cache the vid use
    #RECORD OUR WORK

    weighted_caches.sort(key=lambda tup: tup[1])
    #print video, weighted_caches
    print caches[weighted_caches[0][0]]
    if caches[weighted_caches[0][0]][2] >= size_of_videos[video[0]]:
        print 'put in'

