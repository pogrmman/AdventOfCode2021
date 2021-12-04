#!/usr/bin/env python3
'''Solutions to Day 4 of Advent of Code'''
### Advent of Code Utils ###
import Tools

class Board(object):
    '''Represents a bingo board'''
    def __init__(self, row_list):
        self.board = [row.split() for row in row_list]
        self.board = [[(False, int(number)) for number in row] for row in self.board]

    def mark(self, call):
        '''Mark the number called on the board'''
        for r, row in enumerate(self.board):
            for n, number in enumerate(row):
                if number[1] == call:
                    self.board[r][n] = (True, self.board[r][n][1])

    def check(self):
        '''Check for a bingo WITH NO DIAGONALS'''
        row_length = len(self.board[0])
        count = 0
        # Check rows
        for row in self.board:
            for number in row:
                if number[0]:
                    count += 1
                if count == row_length:
                    return True
            count = 0
        # Check columns
        for c in range(row_length):
            for row in self.board:
                if row[c][0]:
                    count += 1
                if count == row_length:
                    return True
            count = 0
        return False

    def score(self):
        '''Return the sum of the unmarked numbers'''
        unmarked = [number[1] for row in self.board for number in row if not number[0]]
        return sum(unmarked)

    def __str__(self):
        rows = [[number[1] for number in row] for row in self.board]
        rows = '\n'.join([str(row) for row in rows])
        return rows

def return_boards(input_list):
    '''Generator that creates lists of five rows'''
    for i in range(1,len(input_list),6):
        yield input_list[i:i+5]
        
def parse_input(input_list):
    '''Make a list of calls and a list of boards'''
    calls = input_list[0].split(',')
    calls = [int(call) for call in calls]
    boards = []
    for i, board in enumerate(return_boards(input_list[1:])):
        boards.append(Board(board))
    return (calls, boards)

def make_calls(calls, boards):
    '''Begin making calls and return the first one that wins and the call it won on'''
    for call in calls:
        for board in boards:
            board.mark(call)
            if board.check():
                return (call, board)
    return (calls, boards)

def last_to_win(calls, boards):
    '''Return the last board to win and the call it won on'''
    boards = [(False, board) for board in boards]
    for call in calls:
        for i, board in enumerate(boards):
            if not board[0]:
                board[1].mark(call)
                if board[1].check():
                    boards[i] = (True, board[1])
                    winners = [board for board in boards if board[0]]
                    if len(winners) == len(boards):
                        return call, board[1]
    return (calls, boards)

### Run as Script ###
if __name__ == '__main__':
    bingo_list = Tools.read_input('input')
    calls, boards = parse_input(bingo_list)
    call, winner = make_calls(calls, boards)
    if isinstance(winner, list):
        print(f'There was no winner!')
    elif isinstance(winner, Board):
        print(f'Winning score is {winner.score() * call}')
    last_call, last_winner = last_to_win(calls, boards)
    print(f'The last winner had a score of {last_winner.score() * last_call}')
