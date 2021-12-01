def read_input(filename):
    '''Read Advent of Code input file and return a list of input lines'''
    with open(filename, 'r') as f:
        input_lines = f.readlines()
    input_lines = [line.strip() for line in input_lines]
    return input_lines
