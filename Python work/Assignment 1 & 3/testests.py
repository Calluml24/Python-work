# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 12:29:16 2017

@author: w7i78
"""

import csv
from collections import defaultdict

station_info = []

#open up the csv file to create a list 
with open("test.csv") as file:
    info = csv.reader(file)
    next(info)
    for row in info:
        station_info.append(row)

#print(station_info)

#station_id_frm = [index[0] for index in station_info]
#station_id_frm = [int(i) for i in station_id_frm]
#station_id_to = [index[1] for index in station_info]
#station_id_to = [int(i) for i in station_id_to]
#station_time = [index[2] for index in station_info]
#station_time = [int(i) for i in station_time]

#need to convert the info list into integers from strings (maybe a function)
#           
print(station_info)

#print(station_id_frm)
#print(station_id_to)
#print(station_time)

class Graph(object):
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
                       
test = Graph()
for node in station_info:
    test.add_node(node[0])

for node in station_info:
    test.add_edge(node[0],node[1],node[2])
 
print(test.edges)

