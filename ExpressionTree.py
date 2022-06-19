#  File: ExpressionTree.py

#  Description: Expression Tree build time!!

#  Student Name: Neha Kondaveeti

#  Student UT EID: nk8975

#  Course Name: CS 313E

#  Unique Number: 51120

#  Date Created: 04/10

#  Date Last Modified: 04/11

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0
    

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree (object):
    def __init__ (self):
        self.root = Node(None)
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        expr = expr.split()
        # create stack
        thestack = Stack()
        # set current as root node
        current = self.root
        for i in expr:
            # beg para
            if i == "(":
                # create left child node
                current.lChild = Node(None)
                # push i onto stack
                thestack.push(current)
                # set left child node to current
                current = current.lChild
            # end para
            elif i == ")":
                # should reach the end, check stack empty?
                if thestack.is_empty() == False:
                    # take out 
                    current = thestack.pop()
            # operators, global/in class
            elif i in operators:
                current.data = i
                # push onto stack
                thestack.push(current)
                # create right child node
                current.rChild = Node(None)
                # set right child node to current
                current = current.rChild
            # int/float value case
            else:
                current.data = i # no int cast
                current = thestack.pop()

    
    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        # base case, recursion, if not a digit and its an operator
        if aNode.data == operators[0]:
            return float(self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild))
        elif aNode.data == operators[1]:
            return float(self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild))
        elif aNode.data == operators[2]:
            return float(self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild))
        elif aNode.data == operators[3]:
            return float(self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild))
        elif aNode.data == operators[4]:
            return float(self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild))
        elif aNode.data == operators[5]:
            return float(self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild))
        elif aNode.data == operators[6]:
            return float(self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild))
        # if digit, not recursive
        else:
            return float(aNode.data)


    # this function should generate the preorder notation of 
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode, list = []):
        if aNode != None:
            list.append(aNode.data)
            self.pre_order(aNode.lChild)
            self.pre_order(aNode.rChild)
        # loop through list and form string
        string = ""
        for i in list:
            string += str(i) + " "
        return string[:-1]

    
    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode, list = []):
        if aNode != None:
            self.post_order(aNode.lChild)
            self.post_order(aNode.rChild)
            list.append(aNode.data)
        string = ""
        for i in list:
            string += str(i) + " "
        return string[:-1]

    


# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)
    
    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root))

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root))

if __name__ == "__main__":
    main()