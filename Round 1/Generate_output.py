import Greedy


# result should be a dictionary
def print_result(result, file_name):
    with open(file_name, 'w') as f:
        f.write(str(len(result)) + '\n')
        for cache in sorted(result):
            f.write(str(cache) + ' ')
            for vid in result[cache]:
                f.write(str(vid) + ' ')
            f.write('\n')


file_name = 'me_at_the_zoo.in'
# file_name = 'kittens.in'
result = Greedy.greedy(file_name)
print_result(result, 'greedy_' + file_name[:-3] + '.out')
