#  File: Intervals.py

#  Description: Take a set of intervals and collapse all the overlapping intervals, printing the smallest 
# set of non-intersecting intervals

#  Student Name: Neha Kondaveeti

#  Student UT EID: nk8975

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: 01/31

#  Date Last Modified: 01/31

from operator import index
import sys

def merge_tuples (tuples_list):
# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval

    

    tuples_list.sort(key=lambda u: u[0])
    # print(tuples_list)

    #three cases
    #tuples 2 is entirely in tuple 1    -> remove tuple 2 from list
    #tuple 2 and tuple 1 overlap partly -> replace tuple 1 with the intersection and remove tuple 2
    #tuple 2 and tuple 1 don't overlap  -> move on in list

    i = 0
    while i < len(tuples_list)-1:
        j = i + 1
        #while j < len(tuples_list): #can maybe remove this loop
        if tuples_list[j][0] <= tuples_list[i][1]:
        #if tuples_list[j][0] in range(tuples_list[i][0],tuples_list[i][1]):
        #first element of j is in the range of i
            if  tuples_list[j][1] <= tuples_list[i][1]:
                #and second element of j is in range of i
                #remove j from tuples list
                #index j should stay the same to try next tuple
                tuples_list.pop(j)
                # print("1")
                # print(tuples_list)
            elif tuples_list[j][1] > tuples_list[i][1]:
                #and second element of j is outside range of i
                #remove i and j and add a new tuple at i
                #do not increment i but reset j to i + 1
                temp = (tuples_list[i][0],tuples_list[j][1])
                tuples_list[i]=temp
                tuples_list.pop(j)
                j = i + 1
                # print("2")
                # print(tuples_list)
        else:
            #first element of j is outside range of i
            #increment i reset j to i+1
            i += 1
            j = i + 1
            # print("3")
            # print(tuples_list)

    return tuples_list


                

            
                


def sort_by_interval_size (tuples_list):

    for x in range((len(tuples_list))-1):
        # the next value after the x value, denoted as y
        for y in range(x,len(tuples_list)):
            # this comparing next door elements
            # interval size calculations between x and y list
            interval1 = tuples_list[x][1]-tuples_list[x][0]
            interval2 = tuples_list[y][1]-tuples_list[y][0]
            # checking interval sizes against each other
            if interval1 > interval2:
                # swapping by index
                tuples_list[x],tuples_list[y] = tuples_list[y],tuples_list[x]
    return tuples_list


    


def test_cases ():
    # Input: no input
    # Output: a string denoting all test cases have passed
    assert merge_tuples([(1,2)]) == [(1,2)]
    # write your own test cases

    assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
    # write your own test cases

    return "all test cases passed"

def main():
  # open file intervals.in and read the data and create a list of tuples
  # assume file is correct
  # open and read file
    num_tuples = sys.stdin.readline()
    num_tuples = num_tuples.strip()

    # creating tuple list
    # empty list:
    tuples_list = []

    # read rest of lines and append to list

    line = sys.stdin.readline()
    line = line.strip()
    # reads next line, loop through rest of lines
    while line:
        tuple_value = line.split(" ")
        #tuple_value = int(tuple_value)
        #appends the tuple value ranges
        tuples_list.append((int(tuple_value[0]), int(tuple_value[1])))
        # read next line
        line = sys.stdin.readline()
        line = line.strip()
 
  # merge the list of tuples
    #print(sort_by_interval_size(tuples_list))
    merged = merge_tuples(tuples_list)
    merged = str(merged)
    sys.stdout.write(merged)
    sys.stdout.write("\n")

  # sort the list of tuples according to the size of the interval
    
    sorted_tuple = sort_by_interval_size(tuples_list)
    sorted_tuple = str(sorted_tuple)
    sys.stdout.write(sorted_tuple)
    sys.stdout.write("\n") #idk if necessary

  # run your test cases
    '''
    print (test_cases())
    '''

  # write the output list of tuples from the two functions

if __name__ == "__main__":
  main()