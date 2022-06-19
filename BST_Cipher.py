#  File: BST_Cipher.py

#  Description:

#  Student Name: Neha Kondaveeti

#  Student UT EID: nk8975

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 04/18

#  Date Last Modified: 04/18


import sys

class Node(object):
  def __init__(self, data, lChild = None, rChild = None):
    self.data = data
    self.lChild = lChild
    self.rChild = rChild

class Tree (object):
  # the init() function creates the binary search tree with the
  # encryption string. 
  # call the remove other function to have correct string within class
  # If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.

  def __init__ (self, encrypt_str):
    self.root = None
    self.encrypt_str = encrypt_str.lower()
    emptystr = ""
    for i in encrypt_str:
      if ord(i) > 96 and ord(i) < 123 or i == " ":
        emptystr += i
    self.encrypt_str = emptystr
    for i in range(len(self.encrypt_str)):
      self.insert(self.encrypt_str[i])
 
  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
    new = Node(ch)
    if self.root == None:
      self.root = new
      return
    else:
      current = self.root
      parent = self.root
      while current != None:
        parent = current
        if current.data == ch:
          return
        elif ch < current.data:
          current = current.lChild
        else:
          current = current.rChild
      if ch < parent.data:
        parent.lChild = new
        return
      else:
        parent.rChild = new


  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
    current = self.root
    # search val in tree
    if current.data == ch:
      return "*"
    astring = ''
    while current != None and current.data != ch:
      if ch > current.data:
        astring += ">"
        current = current.rChild
      elif ch < current.data:
        astring += "<"
        current = current.lChild
    return astring

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    # opposite of search, oging to be used in decryption
    if len(st) == 0:
      return ""
    else:
      current = self.root
      if st == "*":
        return current.data
      for i in st:
        if current == None:
          return ''
        elif i == ">" and current.rChild != None:
          current = current.rChild
        elif i == "<" and current.lChild != None:
          current = current.lChild
    return current.data

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    encrypt_string = ""
    # make all lower
    st = st.lower()
    for i in st:
      if i in self.encrypt_str:
        encrypt_string += self.search(i) + "!"
      else:
        encrypt_string += str(i)
    final = encrypt_string[:-1]
    return final

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    astring = ""
    dec = st.split("!")
    for i in dec:
      astring += self.traverse(i)
    return astring
  
def main():
  # read encrypt string
  line = sys.stdin.readline()
  encrypt_str = line.strip()

  # create a Tree object
  the_tree = Tree (encrypt_str)

  # read string to be encrypted
  line = sys.stdin.readline()
  str_to_encode = line.strip()

  # print the encryption
  print (the_tree.encrypt(str_to_encode))

  # read the string to be decrypted
  line = sys.stdin.readline()
  str_to_decode = line.strip()
  
  # print the decryption
  print (the_tree.decrypt(str_to_decode))
 
if __name__ == "__main__":
  main()