# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 18:43:58 2017

@author: Callum
"""
class Vertex:
    def __init__(self, id):
        self.id = id
        self.adjacent = {} 	# Adjacency list represented by Set

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def addNeighbour(self, neighbour, weight=0):
        self.adjacent[neighbour] = weight

    def getConnections(self):
        return self.adjacent.keys()  

    def getId(self):
        return self.id

    def getWeight(self, neighbour):
         return self.adjacent[neighbour]
     
class Graph:
    def __init__(self):
        self.vertDict = {}
        self.numVertices = 0
    def __iter__(self):
        return iter(self.vertDict.values())
    def addVertex(self, id):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(id)
        self.vertDict[id] = newVertex
        return newVertex
    def getVertex(self, n):
        if n in self.vertDict:
            return self.vertDict[n]
        else:
            return None
    def addEdge(self, frm, to, cost = 0):
        if frm not in self.vertDict:
            self.addVertex(frm)
        if to not in self.vertDict:
            self.addVertex(to)
        self.vertDict[frm].addNeighbour(self.vertDict[to], cost)
        self.vertDict[to].addNeighbour(self.vertDict[frm], cost)
        
g = Graph()
g.addVertex("a")
g.addVertex("b")
g.addVertex("c")
g.addEdge("a","b",30)
g.addEdge("b","c",50)
g.addEdge("c","a",25)
for v in g:
    for w in v.getConnections():
        vid = v.getId()
        wid = w.getId()
        print ('( %s , %s, %3d)'  % ( vid, wid, v.getWeight(w)))





