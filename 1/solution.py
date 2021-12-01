### Advent of Code Tools ###
import Tools

def count_deeper(input_lines):
    '''Count the number of depth measurements that are deeper than the prior one'''
    initial_depth = int(input_lines[0])
    count = 0
    for depth in input_lines[1:]:
        if int(depth) > initial_depth:
            count += 1
        initial_depth = int(depth)
    return count

if __name__ == '__main__':
    input_lines = Tools.read_input('input')
    count = count_deeper(input_lines)
    print(f'{count} of the depth measurements are deeper than the previous one!')
