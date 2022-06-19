# File: Sugar.py

# Description: Help Alex identify if a graph is a tree.

# Student Name:

# Student EID:

# Course Name: CS 313E

# Unique Number

from operator import truediv
import sys

# Feel free to define any helper functions, if necessary!

# Input: n - total number of vertices in graph, edges - set of all edge connections between vertices
# Output: true/false if graph is valid tree
def isTree(n, edges):
        #TODO
        #if any vertex is connected to any node that the vertex is also connected to
        #visited works well
        # if any both nodes in an edge have been visited then  it's an error
        visited = [False] * n

        for edge in edges: 
            if visited[edge[0]] and  visited[edge[1]]:
                return False
            visited[edge[0]] = True
            visited[edge[1]] = True

        return True

# TAKE CAUTION TO EDIT BELOW
def main():
    n = int(sys.stdin.readline().strip())
    allEdges = []
    for line in sys.stdin:
        edge = list(map(int, line.split(" ")))
        allEdges.append(edge)
    print(isTree(n, allEdges))

if __name__ == "__main__":
    main()
