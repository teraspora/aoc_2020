# aoc 2020

INPUT_EXT = '.txt'
INPUT_DIR = 'data/'
TEST_INPUT_DIR = 'data_test/'

def iget(file):
    with open(file, 'r') as f:
        return f.read()

def get_input(file, test=False):
    return iget((TEST_INPUT_DIR if test else INPUT_DIR) + file[:-3] + INPUT_EXT)
