#  File: Tower.py

#  Description: Calculate optimal number of moves required for Hanoi with 4 needles

#  Student's Name: Neha Kondaveeti

#  Student's UT EID: nk8975

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: 03/5

#  Date Last Modified: 03/11

import math
import sys

# Input: n the number of disks
# Output: returns the number of transfers using four needles
# hanoi tower
def towers (n):
    # Base case
    if n <= 0:
        return 0
    # Base case
    if n == 1:
        return 1
    # Move top n-1 rings to spare, move 1 ring from src to dest, move n-1 rings to dest
    return 2 * towers(n - 1) + 1


def num_moves(n):
    # Base case
    if n <= 0:
        return 0
    # Base case
    if n == 1:
        return 1
    k = n - math.ceil(math.sqrt(2 * n + 1)) + 1
    # Move top k to spare1 and then to dest, can use all 4 needles since they are the smallest rings
    # Move n-k-1 to spare2 and then to dest, can use only 3 needles since can't place over k rings
    return 1 + 2 * num_moves(k) + 2 * towers(n - k - 1)

        

def main():
  # read number of disks and print number of moves
  # print(num_moves(28))
  for line in sys.stdin:
    line = line.strip()
    num_disks = int (line)
    print (num_moves (num_disks))
    
    

if __name__ == "__main__":
  main()
