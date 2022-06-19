#  File: Hiking.py

#  Description: Help Jeff determine if he can finish the Appalachian Trail hike

#  Student Name: Neha Kondaveeti

#  Student UT EID: nk8975

#  Course Name: CS 313E

#  Unique Number: 51120

import sys

def hike(hike_string: str, capacity: int) -> bool:
    # TODO: your code here
    #for each character in hiking string
    #if character is item
    # add to queue
    #if character is encounter
    # pop from queue
    #if pop does not satisfy encounter
    # return false
    stack = []
    for c in hike_string:
        if c == 'b' or c == 'c' or c == 'f':
            if len(stack) < capacity:
                stack.append(c) 
        elif c == 'p':
            if len(stack)==0:
                return False
            item = stack.pop()
            if item != 'b':
                return False
        elif c == 'm':
            if len(stack)==0:
                return False
            item = stack.pop()
            if item != 'c':
                return False
        elif c == 's':
            if len(stack)==0:
                return False
            item = stack.pop()
            if item != 'f':
                return False

    if len(stack)==0:
        return True
    return False
                



# You do not need to modify anything below this line
def main():
    first_line = sys.stdin.readline().split()
    N, W = int(first_line[0]), int(first_line[1])

    for _ in range(N):
        hike_string = sys.stdin.readline().strip()
        print(hike(hike_string, W))

if __name__ == "__main__":
    main()