# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 16:06:30 2017

@author: w7i78
"""

import csv

class Node:
    def __init__(self,ID):
        self.connections={}
        self.id=ID
        
    def add_connection(self,node_to,distance):
        self.connections[node_to]=distance
                        
    def get_connections(self):
        return self.connections
    
    def __str__(self):
        return str(self.id)
         
class Graph:
    def __init__(self):
        self.nodes={}
    
    def add_node(self,value): #i.e input 1, 2 = [(1, {}), (2, {})] (list of dicts?)
        self.nodes[value]=Node(value)
        
    def __str__(self): #when print is run it comes out as follows: [(1, {2: 99999}), (2, {1: 99999})]
        dictlist=[]
        for i in self.nodes:
            dictlist.append((self.nodes[i].id,self.nodes[i].get_connections())) #this is the reference to the Node class
        return str(dictlist)

    def add_connection(self,node_from,node_to,distance):
        self.nodes[node_from].add_connection(node_to,distance)
        self.nodes[node_to].add_connection(node_from,distance)
        
                   
g = Graph()        
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_connection(1,2,99999)
g.add_connection(2,3,10000)
g.add_connection(3,4,500)
g.add_connection(4,1,1000)
print(g)



#station_id = []
#with open("london.stations.csv") as file:
#    info = csv.reader(file)
#    next(info)
#    for row in info:
#        station_id.append(row)  
#station_id = [index[0] for index in station_id]
#
#station_connect = []
#with open("london.connections.csv") as file:
#    info = csv.reader(file)
#    next(info)
#    for row in info:
#        station_connect.append(row)

#print(len(station_id))

#g=Graph()
#for nodes in station_id:
#    g.add_node(nodes)
#
#for info in station_connect:
#    g.add_connection(info[0],info[1],info[3])
#
#print(g)

#Graph is no construceted showing ("station id node" , {joined station id : distance})
#create function that displays the information of 1 node
#use dijkstras algorithm to cycle through the graph to find the shortest path between 2 nodes
        



    
