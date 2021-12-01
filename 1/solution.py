#!/usr/bin/env python3
'''Solutions for Day 1 of Advent of Code 2021'''

### Advent of Code Tools ###
import Tools

### Part 1 Function ###
def count_deeper(input_lines):
    '''Count the number of depth measurements that are deeper than the prior one.'''
    initial_depth = int(input_lines[0])
    count = 0
    for depth in input_lines[1:]:
        if int(depth) > initial_depth:
            count += 1
        initial_depth = int(depth)
    return count

### Part 2 Functions ###
def build_window(input_lines):
    '''Generator that builds a sliding window of 3 input lines.'''
    for i in range(len(input_lines) - 2):
        yield (int(input_lines[i]), int(input_lines[i+1]), int(input_lines[i+2]))

def sliding_window(input_lines):
    '''Count the number of depth windows that are deeper than the prior one.'''
    count = 0
    initial_window = (int(input_lines[0]), int(input_lines[1]), int(input_lines[2]))
    window_sum = sum_window(initial_window)
    for window in build_window(input_lines[1:]):
        new_sum = sum_window(window)
        if new_sum > window_sum:
            count += 1
        window_sum = new_sum
    return count

def sum_window(window):
    '''Return the sum of the window.'''
    return window[0] + window[1] + window[2]

### Run as Script ###
if __name__ == '__main__':
    input_lines = Tools.read_input('input')
    count = count_deeper(input_lines)
    print(f'{count} of the depth measurements are deeper than the previous one!')
    window_count = sliding_window(input_lines)
    print(f'{window_count} of the depth window measurements are deeper than the previous one!')
