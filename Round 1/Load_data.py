import numpy as np
import cPickle as pickle
import os


def load_data(file_name):
    cwd = os.getcwd()
    path = cwd + '\\Processed_data\\'
    with open(path + 'data of ' + file_name + '.p', 'rb') as f:
        data = pickle.load(f)
    table = np.load(path + 'table of ' + file_name + '.npy')
    return data, table
