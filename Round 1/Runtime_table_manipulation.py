import numpy as np
import Load_data as ld
import Data_processing as dp
import Data_processing2 as dp2
import Greedy

#must get full data
def recalc_table(cached_videos, data, table):
    pass


data = dp.read_data('recalculation_example.txt')
trending_total_vid_sizes = dp.read_data('trending_today.in')[1]
print sum(trending_total_vid_sizes)
# table = dp.process_data(data)
# print table
# result = Greedy.greedy(data, table)
# print sorted(result.items())
# print_result(result, 'Greedy_' + file_name[:-3] + '.out', 'Outputs simple Greedy')