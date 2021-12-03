#!/usr/bin/env python3
'''Solutions for Day 2 of Advent of Code 2021'''

### Advent of Code Tools ###
import Tools

### Part 1 ###
class Position(object):
    '''
    Store the position of the submarine

    Provides the following attributes:
    depth -- the submarine's depth
    horizontal -- the submarine's horizontal position
    '''
    def __init__(self):
        '''Initialize the submarine'''
        self.depth = 0
        self.horizontal = 0

    def forward(self, amount):
        '''Move the sumbarine forward by amount'''
        self.horizontal += int(amount)
               
    def down(self, amount):
        '''Move the sumbarine down by amount'''
        self.depth += int(amount)
               
    def up(self, amount):
        '''Move the submarine up by amount'''
        amount = int(amount)
        if self.depth - amount > 0:
            self.depth -= amount
        else:
            self.depth = 0

def execute(instructions, position):
    '''Execute the list of instructions on the given position object'''
    for instruction in instructions:
        instr, amount = instruction.split(' ')
        if instr == 'forward':
            position.forward(amount)
        elif instr == 'down':
            position.down(amount)
        elif instr == 'up':
            position.up(amount)
    return position

### Part 2 ###
class Position2(Position):
    '''
    Store the position of the submarine, following the instructions in Part 2.

    Provides the following attributes:
    aim - the submarine's aim
    depth - the submarine's depth
    horizontal - the submarine's horizontal position
    '''
    def __init__(self):
        '''Initialize the submarine'''
        self.aim = 0
        super().__init__()

    def forward(self, amount):
        '''Move the submarine forward by amount, following the rules in Part 2'''
        amount = int(amount)
        self.horizontal += amount
        self.depth += self.aim * amount
        if self.depth < 0:
            self.depth = 0
        
    def down(self, amount):
        '''Increase the aim by amount, following the rules in Part 2'''
        self.aim += int(amount)

    def up(self, amount):
        '''Decrease the aim by amount, following the rules in Part 2'''
        self.aim -= int(amount)

# Run as script
if __name__ == '__main__':
    instructions = Tools.read_input('input')
    position = execute(instructions, Position())
    print(f'Part 1 solution is {position.depth * position.horizontal}')
    position2 = execute(instructions, Position2())
    print(f'Part 2 solution is {position2.depth * position2.horizontal}')
