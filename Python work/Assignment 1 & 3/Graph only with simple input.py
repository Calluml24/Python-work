# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 22:12:52 2017

@author: Callum
"""

class Graph:
    def __init__(self):
        self.nodes = {}
        self.connections = {}
        self.time = {}
        
    def add_node(self, ID):
        self.nodes[ID] = ID
        
#    def add_connection(self,frm,to,time):
        
        
        
#    def __str__(self):
#        test = []
#        for i in self.nodes:
#            test.append(self.nodes[i])
#        return str(test)
        
#    def __str__(self):
        

g = Graph()        
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
#g.add_connection(1,2,99999)
#g.add_connection(2,3,10000)
#g.add_connection(3,4,500)
#g.add_connection(4,1,1000)
print(g.nodes)
#print(g.connections)
