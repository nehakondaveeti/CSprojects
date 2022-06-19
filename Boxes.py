#  File: Boxes.py

#  Description: 

#  Student Name: Neha Kondaveeti

#  Student UT EID: nk8975

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created:

#  Date Last Modified:

import sys
import functools

# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes (box_list):
  return 

def total(nested_boxes, prev_boxes, idx):
    #Calculates number of ways to nest max number of boxes
    # No boxes inside current box
    if len(prev_boxes[idx]) == 0:
        return 1
    number_of_ways = 0
    # For each possible nested box
    for prev in prev_boxes[idx]:
        # Choose box with max number of nested boxes
        if nested_boxes[prev] == nested_boxes[idx] - 1:
            number_of_ways += total(nested_boxes, prev_boxes, prev)
    return number_of_ways


def compare(box1, box2):
    #Compare function to sort boxes
    #box1, box2: (x, y, z) size of box
    #Returns < 0 if box1 is less than box2
    #Returns > 0 if box1 is greater than box2
    #Returns 0 if box1 is equal to box2
    if box1[0] == box2[0]:
        # First dimension is same, check second dimension
        if box1[1] == box2[1]:
            # Second dimension is same, check third dimension
            return box1[2] - box2[2]
        # Second dimension is different
        return box1[1] - box2[1]
    # First dimension is different
    return box1[0] - box2[0]


# returns True if box1 fits inside box2
def does_fit (box1, box2):
  # Returns True if box1 fits in box2
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # print to make sure that the input was read in correctly
  print (box_list)
  print()

  # sort the box list
  box_list.sort()
  '''
  # Maximum number of nested boxes for each box
  nested_boxes = [1] * num_boxes
  # Indices of boxes that can be nested in each box
  prev_boxes = [[] for _ in range(num_boxes)]
  # Maximum number of nested boxes
  max_nested_boxes = 1
  for i in range(num_boxes):
    # List of boxes that can fit in box i
      can_fit = filter(lambda x: fit(box_list[x], box_list[i]), range(i))
      for idx in can_fit:
        nested_boxes[i] = max(nested_boxes[i], nested_boxes[idx] + 1)
        prev_boxes[i].append(idx)
        max_nested_boxes = max(max_nested_boxes, nested_boxes[i])
  print(max_nested_boxes)
  # Number of way of nesting max_nested_boxes
  number_of_ways = 0
  for i in range(num_boxes):
      if nested_boxes[i] == max_nested_boxes:
          number_of_ways += total(nested_boxes, prev_boxes, i)
  print(number_of_ways)
  '''
  # print the box_list to see if it has been sorted.
  print (box_list)
  print()

  # get the maximum number of nesting boxes and the
  # number of sets that have that maximum number of boxes
  max_boxes, num_sets = nesting_boxes (box_list)

  # print the largest number of boxes that fit
  print (max_boxes)

  # print the number of sets of such boxes
  print(num_sets)

if __name__ == "__main__":
  main()