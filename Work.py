#  File: Work.py 

#  Description: Determine the number of lines that need to be coded before the first cup of coffee

#  Student Name:  Neha Kondaveeti

#  Student UT EID:  nk8975

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 02/18

#  Date Last Modified: 02/18


import sys, time


# lines of code function --> to determine number
def lines(v: int, k: int):
    awake = 1
    total = v
    while (v//(k**awake)) > 0:
        # lines divided by productivity factor
        total += v//(k**awake)
        awake += 1
    return total 


# to determine time


# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def linear_search(n: int, k: int) -> int:
    # use linear search here
    # call the line function
    for v in range(1,n+1):
        if lines(v,k)>=n:
            return v
    
    
    return 0 # placeholder

# Input: int n, the number of lines of code to write
#        int k, the productivity factor
# Output: the number of lines of code that must be 
#         written before the first cup of coffee
def binary_search (n: int, k: int) -> int:
    # check if value below or above middle,
    # cut in half and use upper or lower half
    # keep cutting in half until done
    # call the line function
    low = 1
    high = n
    middle = 0
    while (high >= low):
        middle = (low + high) // 2
        # if higher
        if n > lines(middle, k):
            low = middle + 1
        # in between! return the value
        elif n > lines(middle-1, k) and n <= lines(middle, k):
            return middle
        else:
            # its lower
            high = middle - 1


    return 0 # placeholder

# main has been completed for you
# do NOT change anything below this line
def main():
    num_cases = int((sys.stdin.readline()).strip())

    for i in range(num_cases):
        inp = (sys.stdin.readline()).split()
        n = int(inp[0])
        k = int(inp[1])
        
        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()

# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()