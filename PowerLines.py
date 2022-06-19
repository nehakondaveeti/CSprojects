#  File: PowerLines.py

#  Description: Determines how many power lines must be built to connect everyone to power

#  Student Name:

#  Student UT EID:

#  Course Name: CS 313E

#  Unique Number:


class Vertex(object):
    def __init__(self, label):
        self.label = label
        self.visited = False

    # determine if a vertex was visited
    def was_visited (self):
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

    # add a Vertex with a given label to the graph
    def add_vertex(self, label):
        # add vertex to the list of vertices
        self.Vertices.append(Vertex(label))

        # add a new column in the adjacency matrix
        nVert = len (self.Vertices)
        for i in range (nVert - 1):
          (self.adjMat[i]).append (0)

        # add a new row for the new vertex
        new_row = []
        for i in range (nVert):
          new_row.append (0)
        self.adjMat.append (new_row)

    # add weighted undirected edge to graph
    def add_undirected_edge(self, start, finish, weight=1):
        self.adjMat[start][finish] = weight
        self.adjMat[finish][start] = weight


# Input: houses is a Graph of the neighborhood
#        by default, house 0 is always connected to the power plant
# Output: The minimum number of power lines that must be built to connect
#         all houses to power
def needed_lines(houses: Graph) -> int:
    # YOUR CODE HERE

    #loop through the houses in the graph
    # add it to powered if it has power
    #each house needs at most two lines
    #if it has no edges, connect it to 0 so add one to sum
    # if it is powered it doesn't need any edges
    # if it has edges and isn't powered, add one and mark it and all its neighbors as powered
    powered = [False] * len(houses.Vertices)
    add = [0]*len(houses.Vertices)
    powered[0] = True
    #print(houses.adjMat)
    num = 0

    for house in houses.Vertices:
        if powered[house.label]:
            #go through all its connections and power them
            for to_power in houses.adjMat[house.label]: #every other house connected is too so update those
                if houses.adjMat[house.label][to_power] ==1:
                    if add[to_power] >0:
                        add[to_power] = 0
                    powered[to_power] = True
            #print(powered)
        else: #house is not marked as powered
            for connected in range(len(houses.adjMat[house.label])):
                if houses.adjMat[house.label][connected] ==1: #if the house is connected
                    if powered[connected]: # if that connected house is powered
                        powered[house.label] = True # this house is powered
                        for to_power in houses.adjMat[house.label]: #every other house connected is too so update those
                            if houses.adjMat[house.label][to_power] ==1:
                                if add[to_power] >0:
                                    add[to_power] = 0
                                powered[to_power] = True
                                #when this is done all of its connected houses are marked as powered
            # if this whole loop finishes and it isnt powered yet
            # set it to powered along with all of its connections
            # num +=1


            

        #if the house hasn't been powered yet, its not hooked up
        # loop again and if that house isnt powered
        # add 1 and power all its connections
            if not powered[house.label]:
                add[house.label] = 1
                powered[house.label] =True
                for to_power in houses.adjMat[house.label]: #every other house connected is too so update those
                    if houses.adjMat[house.label][to_power] ==1:
                        add[to_power] = 0
                        # if that house is already powered remove the 1
                        if powered[to_power]:
                            add[house.label] = 0
                        powered[to_power] = True

    for house in houses.Vertices:
        if powered[house.label]:
            #go through all its connections and power them
            for to_power in houses.adjMat[house.label]: #every other house connected is too so update those
                if houses.adjMat[house.label][to_power] ==1:
                    if add[to_power] >0:
                        add[to_power] = 0
                    powered[to_power] = True
            #print(powered)
        else: #house is not marked as powered
            for connected in range(len(houses.adjMat[house.label])):
                if houses.adjMat[house.label][connected] ==1: #if the house is connected
                    if powered[connected]: # if that connected house is powered
                        powered[house.label] = True # this house is powered
                        for to_power in houses.adjMat[house.label]: #every other house connected is too so update those
                            if houses.adjMat[house.label][to_power] ==1:
                                if add[to_power] >0:
                                    add[to_power] = 0
                                powered[to_power] = True
                                #when this is done all of its connected houses are marked as powered
            # if this whole loop finishes and it isnt powered yet
            # set it to powered along with all of its connections
            # num +=1


            

        #if the house hasn't been powered yet, its not hooked up
        # loop again and if that house isnt powered
        # add 1 and power all its connections
            if not powered[house.label]:
                add[house.label] = 1
                powered[house.label] =True
                for to_power in houses.adjMat[house.label]: #every other house connected is too so update those
                    if houses.adjMat[house.label][to_power] ==1:
                        add[to_power] = 0
                        # if that house is already powered remove the 1
                        if powered[to_power]:
                            add[house.label] = 0
                        powered[to_power] = True


        # for each of its connections
            # if the connected house is powered
                #set house to powered
                # for each of its connections
                    #set those houses to powered
                     
        # if the house has a connect

    num = sum(add)

    return num

    pass


# DO NOT MODIFY THIS METHOD
def main():
    houses = Graph()
    num, n = map(int, input().split())
    for house in range(num):
        # add vertex
        houses.add_vertex(house)

    # read in the adjacency matrix
    for _ in range(n):
        start, finish = map(int, input().split())
        houses.add_undirected_edge(start, finish)

    # get the result from your call to needed_lines()
    min = needed_lines(houses)

    # print the result to standard output
    print(min)


if __name__ == "__main__":
    main()
