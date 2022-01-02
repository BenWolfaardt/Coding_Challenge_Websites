class Graph():

    def __init__(self):
        self.maxVertices = 6
        self.vertices = [0] * self.maxVertices
        self.count = 0

    def addNode(self, x):
        if self.count < self.maxVertices:
            self.vertices[self.count] = x
            self.count += 1
        else:
            print("graph full")

    def getNodes(self):
        return self.vertices

# the below will most likely be used in a trees implementation.
# you can then call it into here to be used

class Node():

    def __init__(self, vertex, adjacentLength):
        self.adjacent = [0] * adjacentLength
        self.vertex = vertex
        self.adjacentCount = 0
        self.visited = False

    def addAdjacent(self, x):
        if self.adjacentCount < len(self.adjacent):
            self.adjacent[self.adjacentCount] = x
            self.adjacentCount += 1
        else:
            print("no more adjacent nodes can be added")
        
    def getAdjacent(self):
        return self.adjacent

    def getVertex(self):
        return self.vertex