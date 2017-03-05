import Greedy
import Knapsack
import Load_data as ld
import os
import time


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
file_name = files[1]
data, table = ld.load_data(file_name[:-3])
# result = Greedy.greedy(data, table)
# print_result(result, 'Greedy_spaghetti_' + file_name[:-3] + '.out', 'Outputs simple Greedy')
result = Greedy.greedy_spaghetti(data, table)
print_result(result, 'Greedy_spaghetti_' + file_name[:-3] + '.out', 'Outputs spaghetti Greedy')



# result = Knapsack.knapsack(data, table)
# print_result(result, 'Knapsack_' + file_name[:-3] + '.out') #'Outputs simple Knapsack')

# for f in files:
#     print f
#     start_time = time.time()
#     data, table = ld.load_data(f[:-3])
#     print("Loading: %s seconds" % (time.time() - start_time))
#     start_time = time.time()
#     result = Knapsack.knapsack(data, table)
#     print("Calculating: %s seconds" % (time.time() - start_time))
#     start_time = time.time()
#     print_result(result, 'Knapsack_' + file_name[:-3] + '.out', 'Outputs simple Knapsack')
#     print("Printing: %s seconds" % (time.time() - start_time))

