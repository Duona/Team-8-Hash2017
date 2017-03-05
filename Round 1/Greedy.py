import numpy as np

def greedy(data, table):

    infos, vid_sizes = data[0:2]

    nmOvideos = infos[0]
    nmOendpoints = infos[1]
    nmOrequest = infos[2]
    nmOcaches = infos[3]
    capacity = infos[4]

    weight_table = table
    #returns an array of video indexes there the most valuable video for the cache
    #(the one which saves most time) is on top of the array
    id_table = np.argsort(weight_table, axis=0)[::-1]


    #key = cache_id, list of videos ids stored []
    cached_result = {}

    # for trending today since all caches are connected to each endpoints with same latency
    for cache in xrange(nmOcaches):
        cur_cap = capacity
        for vid_id in id_table[:, cache]:
            #checks if the most valuable video can be stored in current cache and does so if possible
            if vid_sizes[vid_id] <= cur_cap:
                cur_cap -= vid_sizes[vid_id]
                cached_result[str(cache)] = cached_result.get(str(cache), [])
                cached_result[str(cache)].append(vid_id)
            else:
                break

    return cached_result

# doesn't cache the same video twice
# very effective with kittens and trending since most of the caches are connected to most of the endpoints
def greedy_spaghetti(data, table):

    infos, vid_sizes = data[0:2]

    nmOvideos = infos[0]
    nmOendpoints = infos[1]
    nmOrequest = infos[2]
    nmOcaches = infos[3]
    capacity = infos[4]

    weight_table = table
    #returns an array of video indexes there the most valuable video for the cache
    #(the one which saves most time) is on top of the array
    id_table = np.argsort(weight_table, axis=0)[::-1]


    #key = cache_id, list of videos ids stored []
    cached_result = {}

    # for trending today since all caches are connected to each endpoints with same latency
    spaghetti_storedVids = set()
    for cache in xrange(nmOcaches):
        cur_cap = capacity
        for vid_id in id_table[:, cache]:
            #checks if the most valuable video can be stored in current cache and does so if possible
            if vid_sizes[vid_id] <= cur_cap:
                if vid_id not in spaghetti_storedVids:
                    spaghetti_storedVids.add(vid_id)
                    cur_cap -= vid_sizes[vid_id]
                    cached_result[str(cache)] = cached_result.get(str(cache), [])
                    cached_result[str(cache)].append(vid_id)
            else:
                break

    return cached_result
