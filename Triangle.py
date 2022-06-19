#  File: Triangle.py

#  Description:

#  Student Name: Neha Kondaveeti

#  Student UT EID: nk8975

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 03/2

#  Date Last Modified: 03/4

import sys

from timeit import timeit

def brute_helper(grid, sums, cur_sum, row_num, index):
  if row_num == len(grid)-1:
    sums.append(cur_sum+grid[row_num][index])
  else:
    cur_sum = cur_sum +grid[row_num][index]
    sums = brute_helper(grid, sums, cur_sum, row_num+1, index)
    sums = brute_helper(grid, sums, cur_sum, row_num+1, index+1)

  return sums

# returns the greatest path sum using exhaustive search
def brute_force (grid):
  sums = []
  sums = brute_helper(grid,sums, 0, 0,0)
  return max(sums)


# returns the greatest path sum using greedy approach
def greedy (grid):
  total_sum = 0
  last_index = 0
  for x in range(len(grid)):
    if x == 0:
      total_sum += grid[x][0]
      last_index = 0
    else:    
      if grid[x][last_index] > grid[x][last_index + 1]:
        total_sum += grid[x][last_index]
        last_index = last_index
      else:
        total_sum += grid[x][last_index+1]
        last_index = last_index + 1  
  
  return total_sum


# returns the greatest path sum using divide and conquer (recursive) approach
# recursive
def divide_conquer (grid):
  return divide_conquer_helper(grid, 0, 0,0)


def divide_conquer_helper(grid, row_num, index, sum):
  
  if row_num == len(grid):
    # last row
    return sum
  else:
    sum += grid[row_num][index]
    # next branch values
    value = divide_conquer_helper(grid, row_num+1, index,sum)
    value1 = divide_conquer_helper(grid, row_num+1, index+1,sum)
    if value > value1:
      # the max sum index is the newest index
      return divide_conquer_helper(grid, row_num+1, index,sum)
    else:
      return divide_conquer_helper(grid, row_num+1, index+1,sum)
  
# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  # collaspe list
  # if empty
  new_grid = []
  for x in range(len(grid)):
    new_row = []
    for y in range(len(grid[x])):
      if grid[x][y] != 0:
        if x == 0:
          # first row
          new_row.append(grid[x][y])
        else:
          if y==0:
            new_row.append(grid[x][y]+new_grid[x-1][y])
          elif y==x:
            new_row.append(grid[x][y]+new_grid[x-1][y-1])
          else:
            new_row.append(max(new_grid[x-1][y-1],new_grid[x-1][y])+grid[x][y])
      else:
        new_row.append(0)
    new_grid.append(new_row)

  return max(new_grid[len(new_grid)-1])

          


# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()
  
  # check that the grid was read in properly
  
  # output greatest path from exhaustive search
  print("The greatest path sum through exhaustive search is ")
  print(brute_force(grid))
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search
  print('The time taken for exhaustive search in seconds is')
  print (times)
  print()

  # output greatest path from greedy approach
  print("The greatest path sum through greedy search is ")
  print(greedy(grid))
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  print('The time taken for exhaustive search in seconds is')
  print (times)
  print()

  # output greatest path from divide-and-conquer approach
  print("The greatest path sum through recursive search is ")
  print(divide_conquer(grid))
  #times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  #times = times / 10
  # print time taken using divide-and-conquer approach
  print('The time taken for recursive search in seconds is')
  print (times)
  print()

  # output greatest path from dynamic programming 
  print("The greatest path sum through dynamic programming is ")
  print(dynamic_prog(grid))
  #times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  #times = times / 10
  # print time taken using dynamic programming
  print('The time taken for dynamic programming in seconds is')
  print (times)
  print()
if __name__ == "__main__":
  main()
