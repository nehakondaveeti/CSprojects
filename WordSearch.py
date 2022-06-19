#  File: WordSearch.py

#  Description: Find words in a grid. 

#  Student Name: Neha Kondaveeti

#  Student UT EID: nk8975

#  Course Name: CS 313E 

#  Unique Number:

#  Date Created: 01/26

#  Date Last Modified: 01/28

import sys

# Input: None
# Output: function returns a 2-D list that is the grid of letters and
#         1-D list of words to search

def read_input ( ):

  # reading the first number 'n'
  n = sys.stdin.readline()
  n = n.strip()
  n = int(n)
  #print(n)

  # read the space
  sys.stdin.readline()

  # saving the grid as an array
  word_grid = []
  for x in range(0,n):
    grid = sys.stdin.readline()
    grid = grid.strip()
    line = []
    for letter in grid:
      if letter != " ":
        line.append(letter)
    word_grid.append(line)
  #print(word_grid)

  # read the space
  sys.stdin.readline()

  # read number of words
  k = sys.stdin.readline()
  k = k.strip()
  k = int(k)
  #print(k)

  # read the words, compile into list so it is easy to work with
  word_list = []
  for y in range(0,k):
    word = sys.stdin.readline()
    word = word.strip()
    word_list.append(word)
  #print(word_list)

  return word_grid, word_list 

def find_word (word_grid, word):
  # Input: a 2-D list representing the grid of letters and a single
  #        string representing the word to search
  # Output: returns a tuple (i, j) containing the row number and the
  #         column number of the word that you are searching 
  #         or (0, 0) if the word does not exist in the grid

  location = (0,0)
  n = len(word_grid)
  #print(n)
  #right
  for row in range(n):
    for col in range(n-len(word)+1):
      if word_grid[row][col] == word[0]:
        c = col
        old = location
        location = (row+1, col+1)
        for letter in word:
          if letter != word_grid[row][c]:
            location = old
            break
          c+=1

  #left
  for row in range(n):
    for col in range(len(word)-1,n):
      if word_grid[row][col] == word[0]:
        c = col
        old = location
        location = (row+1, col+1)
        for letter in word:
          if letter != word_grid[row][c]:
            location = old
            break
          c+=-1
        
  #down
  for row in range(n-len(word)+1):
    for col in range(n):
      if word_grid[row][col] == word[0]:
        r = row
        old = location
        location = (row+1, col+1)
        for letter in word:
          if letter != word_grid[r][col]:
            location = old
            break
          r+=1
        
  #up
  for row in range(len(word)-1,n):
    for col in range(n):
      if word_grid[row][col] == word[0]:
        r = row
        old = location
        location = (row+1, col+1)
        for letter in word:
          if letter != word_grid[r][col]:
            location = old
            break
          r+=-1

  #down right
  for row in range(n-len(word)+1):
    for col in range(n-len(word)+1):
      if word_grid[row][col] == word[0]:
        r = row
        c = col
        old = location
        location = (row+1, col+1)
        for letter in word:
          if letter != word_grid[r][c]:
            location = old
            break
          r+=1
          c+=1

  #down left
  for row in range(n-len(word)+1):
    for col in range(len(word)-1,n):
      if word_grid[row][col] == word[0]:
        r = row
        c = col
        old = location
        location = (row+1, col+1)
        for letter in word:
          if letter != word_grid[r][c]:
            location = old
            break
          r+=1
          c+=-1

  #up right
  for row in range(len(word)-1,n):
    for col in range(n-len(word)+1):
      if word_grid[row][col] == word[0]:
        r = row
        c = col
        old = location
        location = (row+1, col+1)
        for letter in word:
          if letter != word_grid[r][c]:
            location = old
            break
          r+=-1
          c+=1

  #up left
  for row in range(len(word)-1,n):
    for col in range(len(word)-1,n):
      if word_grid[row][col] == word[0]:
        r = row
        c = col
        old = location
        location = (row+1, col+1)
        for letter in word:
          if letter != word_grid[r][c]:
            location = old
            break
          r+=-1
          c+=-1



    

  return location

    
      

def main():
  # read the input file from stdin
  word_grid, word_list = read_input()
  # print(word_grid)
  # print(word_list)
  #find each word and print its location
  for word in word_list:
    location = find_word(word_grid, word)
    print (word + ": " + str(location))

if __name__ == "__main__":
  main()