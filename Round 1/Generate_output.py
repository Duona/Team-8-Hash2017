import Greedy



#result should be a dictionary
def print_result(result, file_name):
    with open(file_name, 'w') as f:
        f.write(str(len(result))+'\n')
        for cache in sorted(result):
            f.write(str(cache)+' ')
            for vid in result[cache]:
                f.write(str(vid)+' ')
            f.write('\n')

result = Greedy.greedy('trending_today.in')
print_result(result, 'greedy_trending.out')