# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 17:30:58 2017

@author: Callum
"""

#Open up the London Undergroud file - create this as some sort of data?
#Create a Class that constructs a node map of the stations?
#A class that runs the algorithm for calcuating the shortest path?
#added class that runs the closure of tracks and how to navigate around?

import csv

#open up london.stations + create a new variable containing the id + name (try creating a dictionary of id;name)

def CreateNode():
    with open ("london.stations.csv") as file:
        readFile = csv.reader(file, delimiter = ",")
        next(file)   #this skips the header of the csvfile
        IDs = []
        Stations = []
        
        for row in readFile:
            ID = row[0]
            Station = row[3]
                       
            IDs.append(ID)
            Stations.append(Station)
    
#        print(IDs)
#        print(Stations)
        
    for a,b in zip(IDs,Stations):
        print(a,b)
                
#Node = CreateNode()
#print(Node)

#open up the london.connections and create variable containing the id start + finish + length (dictionary/list of ids,idf,line,time)

def CreateDistance():
    with open("london.connections.csv") as file:
        readFile = csv.reader(file, delimiter = ",")
        next(file)
        StartIDs = []
        EndIDs = []
        Lines = []
        Lengths = []
        
        for row in readFile:
            StartID = row[0]
            EndID = row[1]
            Line = row[2]
            Length = row[3]
            
            StartIDs.append(StartID)
            EndIDs.append(EndID)
            Lines.append(Line)
            Lengths.append(Length)
            
    for a,b,c,d in zip(StartIDs,EndIDs,Lines,Lengths):
        print(a,b,c,d)
#
Distance = CreateDistance()
print(Distance)


def Lines():
    with open ("london.lines.csv") as file:
        readFile = csv.reader(file, delimiter = ",")
        next(file)
        Lines = []
        LineNames = []
        
        for row in readFile:
            Line = row[0]
            LineName = row[1]
            
            Lines.append(Line)
            LineNames.append(LineName)
            
    for a,b in zip(Lines,LineNames):
        print(a,b)

#Line = Lines()
#print(Line)


#Create a list containing StartID+name,EndID+name, length

Train_information = []

#convert this into a dictionary when it comes to creating the graph


#look to create 1 main file from all 3 csv files - import global library, 

#Look into what information needs to be passed through the nodes (to create the directed graph)

#create a variable of the all the above to past through the dystra algorithm - bst function

#Class Graph creation

    


