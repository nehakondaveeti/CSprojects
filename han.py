#  File: Tower.py

#  Description: Calculate optimal number of moves required for Hanoi with 4 needles

#  Student's Name: Neha Kondaveeti

#  Student's UT EID: nk8975

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: 03/5

#  Date Last Modified: 03/5

import sys

# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves (n):
    towers(n, 'A', 'B', 'C', 'D')

def towers(n, source, spare1, spare2, dest):
    count = 0
    if n ==1:
        count += 1
    else:
        num_moves(n-1, source, spare2, dest, spare1)
        count += 1
        num_moves(n-1, source, dest, spare1, spare2)
        count += 1
        num_moves(n-1, spare1, spare2, source, dest)
    return count

def main():
  # read number of disks and print number of moves
  for line in sys.stdin:
    line = line.strip()
    num_disks = int (line)
    print (num_moves (num_disks))

if __name__ == "__main__":
  main()
