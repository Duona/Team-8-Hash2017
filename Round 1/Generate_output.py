import Greedy
import Load_data as ld
import os


# result should be a dictionary
def print_result(result, file_name, folder=''):
    cwd = os.getcwd()
    path = cwd + '\\' + folder + '\\'
    with open(path + file_name, 'w') as f:
        f.write(str(len(result)) + '\n')
        for cache in sorted(result):
            f.write(str(cache) + ' ')
            for vid in result[cache]:
                f.write(str(vid) + ' ')
            f.write('\n')

files = ['me_at_the_zoo.in', 'videos_worth_spreading.in', 'trending_today.in', 'kittens.in']
file_name = files[0]
data, table = ld.load_data(file_name[:-3])
result = Greedy.greedy(data, table)
print_result(result, 'Greedy_' + file_name[:-3] + '.out', 'Outputs simple Greedy')
