# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 20:47:06 2017

@author: Callum
"""

import csv

station_info = []

#open up the csv file to create a list 
with open("test.csv") as file:
    info = csv.reader(file)
    next(info)
    for row in info:
        station_info.append(row)

#print(station_info)

station_id = [index[0] for index in station_info]

#print(station_id)

class Node():
    def __init__(self,id):
        self.id = id
        self.adjacent = {}
    def addNeighbour(self,neighbour,weight=0):
        self.adjacent[neighbour] = weight
        
class Graph():
    def __init__(self):
        self.vertDict = {}
        self.numVertices = 0
    
    def addNode(self, id):
        self.numVertices = self.numVertices + 1
        newNode = Node(id)
        self.vertDict = newNode
        return newNode
    
    def addEdge(self,frm,to,cost = 0):
        if frm not in self.vertDict:
            self.addNode(frm)
        if to not in self.vertDict:
            self.addNode(to)
        self.vertDict[frm].addNeighbour(self.vertDict[to], cost)
        self.vertDict[to].addNeighbour(self.vertDict[frm], cost)

#Want to be able to create a for loop that adds a Node to each of the indexs from station_id            
        
    