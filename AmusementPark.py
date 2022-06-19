#  File: AmusementPark.py

#  Student Name: Neha Kondaveeti

#  Student UT EID: nk8975

#  Course Name: CS 313E

#  Unique Number: 51120

class Link (object):
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList (object):
    def __init__(self):
        self.first = None

    def insertFirst(self, data):
        newLink = Link(data)
        newLink.next = self.first
        self.first = newLink

    def insertLast(self, data):
        newLink = Link(data)
        current = self.first

        if (current == None):
            self.first = newLink
            return

        while (current.next != None):
            current = current.next

        current.next = newLink

    def findLink(self, data):
        current = self.first
        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                current = current.next

        return current

    def deleteLink(self, data):
        current = self.first
        previous = self.first

        if (current == None):
            return None

        while (current.data != data):
            if (current.next == None):
                return None
            else:
                previous = current
                current = current.next

        if (current == self.first):
            self.first = self.first.next
        else:
            previous.next = current.next

        return current

# **DO NOT MODIFY ANYTHING ABOVE THIS LINE.**


# Return a linked list with the heights of the children after arranging them
#   based on whether or not they meet the roller coaster height requirement, h.
# You must use the Link and LinkedList classes to complete this question.
# You are **NOT ALLOWED** to use built-in data structures such as lists, sets, dicts,
#   or tuples to store the heights.
def arrangeChildren(heights: LinkedList, h: int) -> LinkedList:
    current = heights.first
    short = LinkedList()
    while current != None:
        #print(current.data)
        if current.data >= h:
            previous = current
            d = previous.data
            current = current.next
            heights.deleteLink(previous.data)
            heights.insertFirst(d)
        elif current.data < h:
            previous = current
            d = previous.data
            current = current.next
            
            heights.deleteLink(previous.data)
            short.insertLast(d)
        else:
            current = current.next    

    s = short.first
    while s != None:
        heights.insertLast(s.data)
        s=s.next
    return heights

# main() is not needed, we will import your code and run it directly
