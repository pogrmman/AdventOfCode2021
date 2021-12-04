#!/usr/bin/env python3
'''Solutions for Day 3 of Advent of Code 2021'''
### Advent of Code Utils ###
import Tools

def most_common(bytestream):
    '''Return a bit-list representing the most common digit at each position'''
    count_list = [0] * len(bytestream[0])
    for byte in bytestream:
        for i, digit in enumerate(byte):
            if digit == '1':
                count_list[i] += 1
    total_bytes = len(bytestream)
    count_list = [1 if digit >= total_bytes / 2 else 0 for digit in count_list]
    return count_list

def flip(byte):
    '''Flip a bit-list'''
    return [1 if digit == 0 else 0 for digit in byte]

def to_decimal(byte):
    '''Convert a bit-list to decimal'''
    out = 0
    for bit in byte:
        out = out * 2 + int(bit)
    return out

def find_rating(rating, bytestream):
    '''
    Find either the o2 or the co2 rating of the submarine

    rating is either the string 'o2' or the string 'co2', determining which one to
    find
    '''
    if rating == 'o2':
        func = lambda stream: most_common(stream)
    elif rating == 'co2':
        func = lambda stream: flip(most_common(stream))
    common = func(bytestream)
    for i in range(len(common)):
        bytestream = [byte for byte in bytestream if int(byte[i]) == common[i]]
        common = func(bytestream)
        if len(bytestream) == 1:
            return bytestream[0]

### Run as Script ###
if __name__ == '__main__':
    bytestream = Tools.read.read_input('input')
    gamma = most_common(bytestream)
    epsilon = flip(gamma)
    gamma = to_decimal(gamma)
    epsilon = to_decimal(epsilon)
    print(f'The power consumption is {gamma * epsilon}')
    o2 = to_decimal(find_rating('o2', bytestream))
    co2 = to_decimal(find_rating('co2', bytestream))
    print(f'The life support rating is {o2 * co2}')
