import numpy as np


def knapsack(data, table, capStep=1):
    infos, vid_sizes = data[0:2]

    nmOvideos = infos[0]
    nmOendpoints = infos[1]
    nmOrequest = infos[2]
    nmOcaches = infos[3]
    capacity = infos[4]


    # key = cache_id, list of videos ids stored []
    cached_result = {}

    for cache in xrange(nmOcaches):
        relevantVids = np.nonzero(table[:, cache])[0]
        dTable = np.ones(((len(relevantVids) + 1), (capacity + 1)))
        # dTable.fill(-1)
        dTable[:, 0] = 0
        dTable[0, :] = 0
        track = np.zeros(((len(relevantVids) + 1), (capacity + 1)), dtype=bool)

        for vid in xrange(1, len(relevantVids) + 1):
            for cap in xrange(1, capacity + 1, capStep):
                #dont forget step
                vidId = relevantVids[vid - 1]
                skipVid = dTable[vid - 1, cap]
                addVid = table[vidId, cache] + dTable[vid - 1, cap - vid_sizes[vidId]]
                # if dTable[vid - 1, cap - vid_sizes[vidId]] == -1:
                #     print 'poop'

                if vid_sizes[vidId] <= cap and addVid > skipVid:
                    dTable[vid, cap] = addVid
                    track[vid, cap] = True
                else:
                    dTable[vid, cap] = skipVid
                    track[vid, cap] = False
        t = capacity
        for vid in xrange(len(relevantVids), 0, -1):
            if track[vid, t] == True:
                vidId = relevantVids[vid - 1]
                cached_result[str(cache)] = cached_result.get(str(cache), [])
                cached_result[str(cache)].append(vidId)
                t -= vid_sizes[vidId]
                # print np.argmax(dTable[:, capacity]), cached_result[str(cache)]

    return cached_result

# TODO make functioning knapsack with certain step of imprecision
# TODO make recalculate table function
# TODO start with caches with most endpoints
# TODO go though caches in random order
