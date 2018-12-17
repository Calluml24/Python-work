# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 22:47:55 2017

@author: Callum
"""

import csv
from collections import defaultdict, deque

station_info = []
with open("london.connections.csv") as file:
    info = csv.reader(file)
    next(info)
    for row in info:
        station_info.append(row)
    
#print(station_info)
#print(len(station_info))

#tidy up the layout of the class graph by creating a __str__ so that it prints out information more clearly

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value[1])
        self.nodes.add(value[0])

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance
                      
                                 
tubeMap = Graph()
for node in station_info:
    tubeMap.add_node(node)

#print(tubeMap.nodes)
#print(len(tubeMap.nodes))

for node in station_info:
    tubeMap.add_edge(str(node[0]), str(node[1]), int(node[3]))

for node in station_info:
    tubeMap.add_edge(str(node[1]), str(node[0]), int(node[3]))

#print(tubeMap.edges)
print(tubeMap.distances) # shows in key, value (from node, to node) then distance

#create function for dijkstras algorithm
#def dijkstra(graph, initial):
#    visited = {initial: 0}
#    path = {}
#
#    nodes = set(graph.nodes)
#
#    while nodes:
#        min_node = None
#        for node in nodes:
#            if node in visited:
#                if min_node is None:
#                    min_node = node
#                elif visited[node] < visited[min_node]:
#                    min_node = node
#        if min_node is None:
#            break
#
#        nodes.remove(min_node)
#        current_weight = visited[min_node]
#
#        for edge in graph.edges[min_node]:
#            try:
#                weight = current_weight + graph.distances[(min_node, edge)]
#            except:
#                continue
#            if edge not in visited or weight < visited[edge]:
#                visited[edge] = weight
#                path[edge] = min_node
#
#    return visited, path
#
#
#def shortest_path(graph, origin, destination):
#    visited, paths = dijkstra(graph, origin)
#    full_path = deque()
#    _destination = paths[destination]
#
#    while _destination != origin:
#        full_path.appendleft(_destination)
#        _destination = paths[_destination]
#
#    full_path.appendleft(origin)
#    full_path.append(destination)
#
#    return visited[destination], list(full_path)
#                                      
#                    
#    
#create funtion that generates the shortest path