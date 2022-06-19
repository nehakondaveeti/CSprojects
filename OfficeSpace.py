#  File: OfficeSpace.py

#  Description: Let employees request spaces and determine what spaces are availible, contested, and uncontested

#  Student Name: Neha Kondaveeti

#  Student UT EID: nk8975

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 02/08

#  Date Last Modified: 02/08
import sys
    
# Input: a rectangle which is a tuple of 4 integers (x1, y1, x2, y2)
# Output: an integer giving the area of the rectangle
def area (rect):
    x1,y1,x2,y2 = rect
    length = abs(int(x2-x1))
    width = abs(int(y2-y1))
    area = int(length * width)
    return area 

# Input: two rectangles in the form of tuples of 4 integers
# Output: a tuple of 4 integers denoting the overlapping rectangle.
#         return (0, 0, 0, 0) if there is no overlap
def overlap (rect_1, rect_2):
    # set ranges of original rectangle 
    x1, y1, x2, y2 = rect_1
    x3, y3, x4, y4 = rect_2
    inner_rect_x1 = max(x1, x3)
    inner_rect_y1 = max(y1, y3)
    inner_rect_x2 = min(x2, x4)
    inner_rect_y2 = min(y2, y4)
    if inner_rect_x1 > inner_rect_x2:
        return (0,0,0,0)
    if inner_rect_y1 > inner_rect_y2: 
        return (0,0,0,0)
    else:
        return (inner_rect_x1, inner_rect_y1, inner_rect_x2, inner_rect_y2)


# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the unallocated 
#         space in the office
def unallocated_space (bldg):
    un = 0
    for j in range(len(bldg)):
            for i in range(len(bldg[j])):
                if(bldg[j][i]==0):
                    un +=1
    return un
    
    
    


# Input: bldg is a 2-D array representing the whole office space
# Output: a single integer denoting the area of the contested 
#         space in the office
def contested_space (bldg):
    un = 0
    for j in range(len(bldg)):
            for i in range(len(bldg[j])):
                if(bldg[j][i]>1):
                    un +=1
    return un
# Input: bldg is a 2-D array representing the whole office space
#        rect is a rectangle in the form of a tuple of 4 integers
#        representing the cubicle requested by an employee
# Output: a single integer denoting the area of the uncontested 
#         space in the office that the employee gets
def uncontested_space (bldg, rect):
    un = 0
    x1,y1,x2,y2 = rect
    # fix y-value because we are doing grid flipped
    y1 = int(y1)#abs(int(y1) - height)
    y2 = int(y2)#abs(int(y2) - height)
    x1 = int(x1)
    x2 = int(x2)
        
    for j in range(y1,y2):
        for i in range(x1,x2):
            if(bldg[j][i]==1):
                    un +=1
    return un

# Input: office is a rectangle in the form of a tuple of 4 integers
#        representing the whole office space
#        cubicles is a list of tuples of 4 integers representing all
#        the requested cubicles
# Output: a 2-D list of integers representing the office building and
#         showing how many employees want each cell in the 2-D list
def request_space (office, cubicles):
    x,y,x0,y0 = office
    #print(x0)
    width = int(x0) #+ 1
    height = int(y0) #+ 1
    # bldg filled with 0s
    bldg = []
    for i in range(0,height):
        # create a new list of rows
        inside = 0
        rows = []
        for j in range(width):
            #print(j)
            rows.append(inside)
        bldg.append(rows)
        #print(i)
    #print(bldg)
    for coor in cubicles:
        #print(coor)
        x1,y1,x2,y2 = coor
        # fix y-value because we are doing grid flipped
        y1 = int(y1)#abs(int(y1) - height)
        y2 = int(y2)#abs(int(y2) - height)
        x1 = int(x1)
        x2 = int(x2)
        
        for j in range(y1,y2):
            for i in range(x1,x2):
                bldg[j][i] +=1
    #print(bldg)
    return bldg
                
# Input: no input
# Output: a string denoting all test cases have passed
#def test_cases ():
  #assert area ((0, 0, 1, 1)) == 1
  # write your own test cases

  #return "all test cases passed"

def main():
  # read the data
    # size of office space
    office_size = sys.stdin.readline()
    w, h = office_size.split(" ")
    w = int(w.strip()) # feet west-east
    h = int(h.strip()) # feet south-north

    # create bldg with w * h dimensions
    size = (0,0,w,h)
    #bldg = [[0]*(w+1)]*(h+1)
    #print(len(bldg))

    # number of employees

    num_employees = sys.stdin.readline()
    num_employees = int(num_employees.strip())

    # cubicle placements
    my_dict = {}
    for n in range(num_employees):
        name = sys.stdin.readline()
        name, x1, y1, x2, y2 = name.split(" ")
        name = name.strip()
        x1 = int(x1.strip())
        y1 = int(y1.strip())
        x2 = int(x2.strip())
        y2 = int(y2.strip())
        coordinates = (x1,y1,x2,y2)
        my_dict[name] = coordinates

  # run your test cases
  #'''
  #print (test_cases())

    #print(request_space((0, 0, 2, 2),[(0, 0, 2, 1),(0, 0, 1, 2)]))

  #'''

  # print the following results after computation
    #print(my_dict.values)
    cubes = []
    for value in my_dict.values():
        cubes.append(value)
    #print(cubes)
    bldg = request_space(size,cubes)
    #print(bldg)
  # compute the total office space
    #total_office_space = w * h
    #print("Total " + str(total_office_space))
    sys.stdout.write("Total "+ str(area((0,0,w,h))))
    sys.stdout.write('\n')

  # compute the total unallocated space
    sys.stdout.write('Unallocated '+ str(unallocated_space(bldg)))
    sys.stdout.write('\n')
  # compute the total contested space
    sys.stdout.write('Contested '+ str(contested_space(bldg)))
    sys.stdout.write('\n')
  # compute the uncontested space that each employee gets
    for key in my_dict.keys():
        sys.stdout.write(key + " " + str(uncontested_space(bldg, my_dict[key])))
        sys.stdout.write('\n')

if __name__ == "__main__":
  main()