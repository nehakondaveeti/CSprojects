#  File: TestBinaryTree.py

#  Description: Adding to Node and Tree class and calculated level, height, equality, and length

#  Student Name: Neha Kondaveeti

#  Student UT EID: nk8975

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 04/12

#  Date Last Modified: 04/13

import sys

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = None

    def insert(self, data: int):
        new = Node(data)
        if self.root == None:
            self.root = new
            return
        else:
            current = self.root
            parent = self.root
            while current != None:
                parent = current
                if data < current.data:
                    current = current.lChild
                else:
                    current = current.rChild
            if data < parent.data:
                parent.lChild = new
            else:
                parent.rChild = new

    # Returns true if two binary trees are similar
    # recursion
    def is_similar (self, pNode):
        first = self.root
        second = pNode.root
        # base case
        # if both trees empty, return true
        def compare(first, second):
            if first == None and second == None:
                return True
            # first empty second not
            elif first == None and second != None:
                return False
                # first not and second empty
            elif first != None and second == None:
                return False
            # if they are the same
            elif first.data == second.data:
                return True
            else:
                return compare(first.lChild, second.rChild) and compare(first.rChild, second.lChild)
        return compare(first, second)
                
    # Returns a list of nodes at a given level from left to right
    def get_level (self, level): 
        first = self.root 
        yuh = []
        def helper(first, level):
            if first == None:
                return
            if first != None and level == 0:
                yuh.append(first)
            else:
                helper(first.lChild, level -1)
                helper(first.rChild, level -1)
        helper(first, level)
        return yuh


    # Returns the height of the tree
    def get_height (self): 
        first = self.root
        def height(first):
            if first == None:
                return -1
            else:
                # to traverse, call function
                # get right tree depth
                right = height(first.rChild)
                # get left tree depth
                left = height(first.lChild)
            return max(left, right) + 1
        return height(first)


    # Returns the number of nodes in the left subtree and
    # the number of nodes in the right subtree and the root
    def num_nodes (self):
        # traverse down tree
        # base case
        first = self.root
        def num(first):
            if first == None:
                return 0
            else:
                return 1 + num(first.lChild) + num(first.rChild)
        return num(first)


def main():
    # Create three trees - two are the same and the third is different
    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree1_input = list (map (int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree2_input = list (map (int, line)) 	# converts elements into ints

    line = sys.stdin.readline()
    line = line.strip()
    line = line.split()
    tree3_input = list(map (int, line)) 	# converts elements into ints
    
    # create tree 1 object
    treeA = Tree()
    # insert nodes into tree
    for i in tree1_input:
        treeA.insert(i)

    # create tree 2 object
    treeB = Tree()
    # insert nodes into tree
    for i in tree2_input:
        treeB.insert(i)
    
    # create tree 3 object
    treeC = Tree()
    # insert nodes into tree
    for i in tree3_input:
        treeC.insert(i)
        
    # Test your method is_similar()

    print(treeA.is_similar(treeB))
    print(treeB.is_similar(treeC))
    print(treeC.is_similar(treeA))

    # Print the various levels of two of the trees that are different
    # print A & C

    print(treeA.get_level(2))
    print(treeB.get_level(2))
    print(treeC.get_level(2))

    # Get the height of the two trees that are different

    print(treeA.get_height())
    print(treeC.get_height())

    # Get the total number of nodes a binary search tree

    print(treeA.num_nodes())
    print(treeB.num_nodes())
    print(treeC.num_nodes())

if __name__ == "__main__":
    main()