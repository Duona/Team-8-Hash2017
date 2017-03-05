import numpy as np
import cPickle as pickle
import os
import time
import Data_processing
import Data_processing2


def save_data(file_name, data, table):
    cwd = os.getcwd()
    path = cwd + '\\Processed_data\\'
    with open(path + 'data of ' + file_name + '.p', 'wb') as f:
        pickle.dump(data, f, protocol=2)
    np.save(path + 'table of ' + file_name, table)

def save_essential_data(file_name, data, table):
    cwd = os.getcwd()
    path = cwd + '\\Processed_data\\'
    with open(path + 'data of ' + file_name + '.p', 'wb') as f:
        pickle.dump(data[0:2], f, protocol=2)
    np.save(path + 'table of ' + file_name, table)

files = ['me_at_the_zoo.in', 'videos_worth_spreading.in', 'trending_today.in', 'kittens.in']
file_name = files[0]

#Data processing 1
# for f in files:
#     print f
#     start_time = time.time()
#     data = Data_processing.read_data(f)
#     print("Reading: %s seconds" % (time.time() - start_time))
#     start_time = time.time()
#     table = Data_processing.process_data(data)
#     print("Processing: %s seconds" % (time.time() - start_time))
#     start_time = time.time()
#     save_data(f[:-3], data, table)
#     print("Saving: %s seconds" % (time.time() - start_time))

#Data processing 2
for f in files:
    print f
    start_time = time.time()
    data = Data_processing2.read_data(f)
    print("Reading: %s seconds" % (time.time() - start_time))
    start_time = time.time()
    table = Data_processing2.process_data(data)
    print("Processing: %s seconds" % (time.time() - start_time))
    start_time = time.time()
    save_essential_data(f[:-3] + '2', data, table)
    print("Saving: %s seconds" % (time.time() - start_time))
