#  File: TopoSort.py

#  Description: 

#  Student Name: Neha Kondaveeti

#  Student UT EID: nk8975

#  Course Name: CS 313E

#  Unique Number: 

#  Date Created:

#  Date Last Modified:

import sys

class Stack (object):
    def __init__ (self):
        self.stack = []

    # add an item to the top of the stack
    def push (self, item):
        self.stack.append (item)

  # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

  # check the item on the top of the stack
    def peek (self):
        return self.stack[-1]

  # check if the stack if empty
    def is_empty (self):
        return (len (self.stack) == 0)

  # return the number of elements in the stack
    def size (self):
        return (len (self.stack))


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue (self, item):
        self.queue.append (item)

    # remove an item from the beginning of the queue
    def dequeue (self):
        return (self.queue.pop(0))

    # check if the queue is empty
    def is_empty (self):
        return (len (self.queue) == 0)

    # return the size of the queue
    def size(self):
        return len(self.queue)
        

class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False
    
    # determine if a vertex was visited
    def was_visited(self):
        return self.visited

    # determine the label of the vertex
    def get_label(self):
        return self.label
    
    # string representation of the vertex
    def __str__(self):
        return str(self.label)

   
class Graph(object):
    def __init__(self):
        self.Vertices = []
        self.adjMat = []

    # check if a vertex is already in the graph
    def has_vertex(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == self.Vertices[i].get_label():
                return True
        return False

    # given the label get the index of a vertex
    def get_index(self, label):
        nVert = len(self.Vertices)
        for i in range(nVert):
            if label == self.Vertices[i].get_label():
                return i
        return -1

    # add a vertex with a given label to the graph
    def add_vertex (self, label):
        if self.has_vertex(label):
            return 

        # add vertex to the list
        self.Vertices.append(Vertex(label))

        # add a new column in adjacentcy matrix
        nVert = len(self.Vertices)
        for i in range(nVert -1):
            self.adjMat[i].append(0)

        # add new row for the new vertix
        new_row = []
        for i in range(nVert):
            new_row.append(0)
        self.adjMat.append(new_row)

    # add weighted directed edge to graph
    def add_directed_edge (self, start, finish, weight = 1):
        self.adjMat[start][finish] = weight

    # add weighted undirected edge to graph
    def add_undirected_edge (self, start, finish, weight = 1): # default weight of 1
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight

    # return an unvisited vertex adjacent to vertex v (index)
    def get_adj_unvisited_vertex (self, v):
        nVert = len (self.Vertices)
        for i in range (nVert):
            if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).was_visited()):
                return i
        return -1
    
      # do a depth first search in a graph
    def dfs (self, v):
    # create the Stack
        theStack = Stack ()

        # mark the vertex v as visited and push it on the Stack
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])
        theStack.push (v)

        # visit all the other vertices according to depth
        while (not theStack.is_empty()):
        # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (theStack.peek())
            if (u == -1):
                u = theStack.pop()
            else:
                (self.Vertices[u]).visited = True
                print (self.Vertices[u])
                theStack.push (u)

        # the stack is empty, let us rest the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False

    # do the breadth first search in a graph
    def bfs (self, v):
        # create queue
        breadth = Queue()

        # mark vertices as visited
        (self.Vertices[v]).visited = True
        print (self.Vertices[v])
        # enqueue
        breadth.enqueue(v)

        # visit all other vertices according to depth
        while (not breadth.is_empty()):
            vert = breadth.dequeue()
            # get an adjacent unvisited vertex
            u = self.get_adj_unvisited_vertex (vert)
            while u != -1:
                (self.Vertices[u]).visited = True
                print (self.Vertices[u])
                breadth.enqueue(u)
                u = self.get_adj_unvisited_vertex (vert)
        # the queue is empty, let us rest the flags
        nVert = len (self.Vertices)
        for i in range (nVert):
            (self.Vertices[i]).visited = False
    
    # determine if a directed graph has a cycle
    # this function should return a boolean and not print the result
    def has_cycle (self):
        # recursion staack
        stack = Stack()
        # find vertices not vistied and adj, call function and check if true
        for i in range(len(self.Vertices)):
            # if already marked, return true
            # if the helper after its run recursion is true 
            if self.cycle_helper(i, stack) == True:
                return True
            else: # calls recursion fucntion is anything returns true
                return False
    
    def cycle_helper(self, i, astack):
        # intialize current index or vertex visited
        # mark current node at visited
        self.Vertices[i].visited = True
        # push onto stack
        astack.push(self.Vertices[i]) 
        # make vertex in adj mat
        v = self.adjMat[self.get_index(self.Vertices[i])]
        # list to store values
        alist = []
        # loop to add correct values to list
        for j in v:
            # base case
            if j == 0:
                break
            else:
                alist.append(self.Vertices[j])
        # loop through list
        for k in alist:
            # if something in stack and visited
            if k.visited == True:
                    if astack[k] != None:
                        # if not visited, call recursion
                        if k.visited == False:
                            return True
            elif self.cycle_helper(k, astack):
                return True
        # set them to unvisited after
        for l in range(len(self.Vertices)):
            self.Vertices[l].visited = False
                
    # return a list of vertices after a topological sort
    # this function should not print the list
    def toposort (self):
        pass

    def toposort_helper(self):
        pass

    def delete_vertex(self, vertexLabel):
        # remove it from vertex list and remove corresponding row and column
        city = vertexLabel
        # get city index
        ind = self.get_index(city)
        # remove from vertices list
        self.Vertices.pop(ind)
        # row
        self.adjMat.pop(ind)
        # column
        for i in range(len(self.adjMat)):
            self.adjMat[i].pop(ind)


def main():
    # create the Graph object
    topo = Graph()

    # open the topo file
    new = open("topo.txt", "r")

    # read the number of vertices
    line = new.readline()
    line = line.strip()
    num_v = int (line)

    # read the vertices to the list of Vertices
    for i in range (num_v):
        line = new.readline()
        point = line.strip()
        topo.add_vertex (point)

    # read the number of edges
    line = new.readline()
    line = line.strip()
    num_e = int (line)

    # read each edge and place it in the adjacency matrix
    for i in range (num_e):
        line = new.readline()
        edge = line.strip()
        edge = edge.split()
        fromVertex = int(topo.get_index(edge[0]))
        toVertex = int(topo.get_index(edge[1]))
        weight = int (1)
        # coordinates
        topo.add_directed_edge (fromVertex, toVertex, weight)

    # get the index of the starting vertex

    # test if a directed graph has a cycle
    if (topo.has_cycle()):
        print ("The Graph has a cycle.")
    else:
        print ("The Graph does not have a cycle.")
        vertex_list = topo.toposort()
        print ("\nList of vertices after toposort")
        print(vertex_list)
    new.close()
    
if __name__ == "__main__":
    main()