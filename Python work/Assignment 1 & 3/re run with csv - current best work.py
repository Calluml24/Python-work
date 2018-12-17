# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 18:02:58 2017

@author: w7i78
"""

import csv

class Node():
    def __init__(self, value):
        self.connections = {}
        self.id = value
    
    def __str__(self):
        return str(self.id)
        
    def add_connection(self, to, time=0):
        self.connections[to] = time
                        
    def get_connections(self):
        return self.connections
        
    def get_nodes(self):
        return self.id
    
#    def getNode(self):
#        for node in self:
#            return node.get_connections()
                
class Graph():
    def __init__(self):
        self.nodes = {}
    
    def __iter__(self):
        return iter(self.nodes.values())
        
    def __str__(self): #all this does is create how it is printed out - doesnt affect input
        stationlist = []
        for eachid in self.nodes:
            stationlist.append((self.nodes[eachid].id, self.nodes[eachid].get_connections()))
        return str(stationlist)
           
    def add_node(self,value):
        self.nodes[value] = Node(value) #means that {} of nodes = Node(value input)- then links that to the Node (self.id for all values)
        
    def add_connection(self,frm,to, time):
        self.nodes[frm].add_connection(to, time)
        self.nodes[to].add_connection(frm, time)
        
#    def getNodes(self):
#        return list(self.nodes.keys()) #this allows to index specific Nodes
    

    def dfs_paths(graph, start, goal):
        stack = [(start, [start])]
        visited = set()
        while stack:
            (node, path) = stack.pop()
            if node not in visited:
                if node == goal:
                    return path
                visited.add(node)
                for neighbour in graph[node]:
                    stack.append((neighbour, path + [neighbour]))
                    
#.................................................................................................................................
#csv opening + translation into the Graph class    
    
station_id = []
with open("london.stations.csv") as file:
    info = csv.reader(file)
    next(info)
    for row in info:
        station_id.append(row)  
station_id = [index[0] for index in station_id]

station_connect = []
with open("london.connections.csv") as file:
    info = csv.reader(file)
    next(info)
    for row in info:
        station_connect.append(row)
        
#print(station_id)
#print(station_connect)

tubeMap = Graph()
for nodes in station_id:
    tubeMap.add_node(nodes)

for info in station_connect:
    tubeMap.add_connection(info[0],info[1],info[3])
    
#.................................................................................................................................

#print(Node(tubeMap).id)  #use class Node to look into the ids of the Tubemap class Graph instance (assigned as value)

#for v in tubeMap:
#    print(v.get_nodes())
#for v in tubeMap:
#    print(v.get_connections())
#for v in tubeMap:
#    print(v.get_nodes(), v.get_connections())
#    
#ask someone how i could potentially reference just the first node from here? 
#try a simple alogrithm that shows you a path from 1 node to another before working on the shortest path

#print (tubeMap)
#a = tubeMap.getNodes()
#print(a[1])

test = Graph()        
test.add_node(1)
test.add_node(2)
test.add_node(3)
test.add_node(4)
test.add_connection(1,2,99999)
test.add_connection(2,3,10000)
test.add_connection(3,4,500)
test.add_connection(4,1,1000)
print(test)
#print(Node(test).id)



#Djikstra sorting algorithm
