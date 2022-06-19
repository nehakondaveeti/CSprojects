#  File: TestLinkedList.py

#  Description: Methods for Linked Lists

#  Student Name: Neha Kondaveeti

#  Student UT EID: nk8975

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 04/4

#  Date Last Modified: 04/4

class Link (object):
  # link class
  def __init__(self, data, next = None):
    self.data = data
    self.next = next


class LinkedList (object):
  # create a linked list
  # you may add other attributes
  def __init__ (self):
    self.first = None

  # get number of links 
  def get_num_links (self):
    # setting to first
    current = self.first
    counter = 0
    while current != None:
      current = current.next
      counter += 1
    return counter
  
  # add an item at the beginning of the list
  def insert_first (self, data): 
    newLink = Link(data)
    newLink.next = self.first
    self.first = newLink

  # add an item at the end of a list
  def insert_last (self, data): 
    newLink = Link(data)
    current = self.first

    if current == None:
      self.first = newLink
      return ""

    while (current.next != None):
      current = current.next
    
    current.next = newLink
  
    return ""

  # add an item in an ordered list in ascending order
  # assume that the list is already sorted
  def insert_in_order (self, data): 
    '''
    current = self.first
    if current == None:
      new = Link(data)
      new.data = data
      self.first = new
    
    while current.next != None:
      if current.next.data > data:
        break
      if current.next.data <= data:
        if current.next == None:
          current = current.next
      current = current.next
    new = Link(data)
    new.data = data
    new.next = current.next
    current.next = new
    '''
    new = Link(data)
    current = self.first
    if current == None:
      self.first = new
    else:
      current = self.first
      past = current
      while current.data < data:
        past = current
        current = current.next
        if current == None:
          self.first.next = new
          self.first = new
          break
      if current == self.first:
        self.first = new
      else:
        past.next = new
      new.next = current

  # search in an unordered list, return None if not found
  def find_unordered (self, data): 
    current = self.first
    if current == None:
      return None
    else:
      while current.data != data:
        if current.next == None:
          return None
        else:
          current = current.next
      return current

  # Search in an ordered list, return None if not found
  def find_ordered (self, data): 
    current = self.first
    if current == None:
      return None
    else:
      while current.data != data:
        if current.data > data:
          return None
        current = current.next
        if current == None:
          return None
      return current
        

  # Delete and return the first occurrence of a Link containing data
  # from an unordered list or None if not found
  def delete_link (self, data):
    current = self.first
    if current == None:
      return None
    while (current.data != data):
      if current.next == None:
        return None
      else:
        current = current.next
    if current == self.first:
      self.first = self.first.next
    else:
      self.first.next = current.next
    
    return current

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    current = self.first
    string = ""
    counter = 0
    while current != None:
      string += str(current.data) + "  "
      current = current.next
      counter += 1
      if counter % 10 == 0:
        string += '\n'
    return string


  # Copy the contents of a list and return new list
  # do not change the original list
  def copy_list (self):
    # create a copy
    thecopy = LinkedList()
    current = self.first
    if current == None:
      return None
    # loop through
    while current != None:
      # append it kinda with method
      thecopy.insert_last(current.data)
      # next one
      current = current.next
    return thecopy

  # Reverse the contents of a list and return new list
  # do not change the original list
  def reverse_list (self): 
    reverse_list = LinkedList()
    current = self.first
    while current != None:
      reverse_list.insert_first(current.data)
      current = current.next
    return reverse_list

  # Sort the contents of a list in ascending order and return new list
  # do not change the original list
  def sort_list (self): 
    new = LinkedList()
    current = self.first
    if current == None:
      return None
    while current != None:
      new.insert_in_order(current.data)
      current = current.next
    return new
    
  # Return True if a list is sorted in ascending order or False otherwise
  def is_sorted (self):
    current = self.first
    future = self.first
    if current == None:
      return None
    while current != None:
      future = future.next
      if current.data > future.data:
        return False
      elif current.data < future.data:
        return True
      elif future.data == None:
        break
      current = current.next
      future = future.next


  # Return True if a list is empty or False otherwise
  def is_empty (self): 
    if self.first == None:
      return True
    else:
      return False

  # Merge two sorted lists and return new list in ascending order
  # do not change the original lists
  def merge_list (self, other): 
    # make a copy list
    new = LinkedList()
    current = self.first
    current2 = other.first
    if current == None and current2 == None:
      return None
    while current != None and current2 != None:
      if current.data > current2.data:
        new.insert_last(current2.data)
        current2 = current2.next
      else:
        new.insert_last(current.data)
        current = current.next
    while current2 != None:
      new.insert_last(current2.data)
      current2 = current2.next
    while current != None:
      new.insert_last(current.data)
      current = current.next
    return new
  
  # Test if two lists are equal, item by item and return True
  def is_equal (self, other):
    if self.first == None and other.first == None:
      return True
    else:
      current = self.first
      other = other.first
      while current != None and other != None:
        if current.data != other.data:
          return False
        current = current.next
        other = other.next
      return True

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  # do not change the original list
  def remove_duplicates (self):
    current = self.first
    new = LinkedList()
    if current == None :
      return None
    while current != None:
      if new.find_unordered(current.data) == None:
        new.insert_last(current.data)
      current = current.next
    return new

def main():
  # Test methods insert_first() and __str__() by adding more than
  # 10 items to a list and printing it.

  # Test method insert_last()

  # Test method insert_in_order()

  # Test method get_num_links()

  # Test method find_unordered() 
  # Consider two cases - data is there, data is not there 

  # Test method find_ordered() 
  # Consider two cases - data is there, data is not there 

  # Test method delete_link()
  # Consider two cases - data is there, data is not there 

  # Test method copy_list()

  # Test method reverse_list()

  # Test method sort_list()

  # Test method is_sorted()
  # Consider two cases - list is sorted, list is not sorted

  # Test method is_empty()

  # Test method merge_list()

  # Test method is_equal()
  # Consider two cases - lists are equal, lists are not equal

  # Test remove_duplicates()
  pass


if __name__ == "__main__":
  main()