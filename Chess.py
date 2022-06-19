#  File: Chess.py

#  Description: How many queens can fit on n board so no queen can caputure another

#  Student Name: Neha Kondaveeti

#  Student UT EID: nk8975

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 03/17

#  Date Last Modified: 03/20

import sys

class Queens (object):

# takes in board size and determines # of queens that can fit without capturing another

    def __init__ (self, n):
        self.board = []
        self.n = n
        # counter 
        self.counter = 0

        # new boards
        for i in range (self.n):
            row = []
            for j in range (self.n):
                row.append ('*')
            self.board.append (row)

    # print the board
    def print_board (self):
        for i in range (self.n):
            for j in range (self.n):
                print (self.board[i][j], end = ' ')
            print ()
        print ()

    # check if a position on the board is valid
    # check if no queen will capture another
    def is_valid (self, row, col):
        for i in range (self.n):
            if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
                return False
        for i in range (self.n):
            for j in range (self.n):
                row_diff = abs (row - i)
                col_diff = abs (col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True
    
    # do the recursive backtracking
    # DO WORK HERE
    def recursive_solve (self, col):
        if (col == self.n):
            # count number of queens
            #self.print_board()
            self.counter += 1
        else:
            for i in range (self.n):
                if (self.is_valid (i, col)):
                    self.board[i][col] = 'Q'
                    if (self.recursive_solve(col + 1)):
                        return True
                    self.board[i][col] = '*'
            return False

  # if the problem has a solution print the board
  # DO WORK HERE
    def solve (self):
        self.recursive_solve(0)
        print(self.counter)
        

def main():
    # read the size of the board
    line = sys.stdin.readline()
    line = line.strip()
    n = int (line)

    # create a chess board
    game = Queens (n)

    # place the queens on the board and count the solutions
    #game.print_board()
  
    # print the number of solutions
    game.solve()
    #print(game.queens())


 
if __name__ == "__main__":
  main()
