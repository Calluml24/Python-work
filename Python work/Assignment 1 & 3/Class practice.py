# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:32:55 2017

@author: w7i78
"""

import math

#class Point:
#    def __init__(self):
#        self.x = 0   #this will create the instance.x as 0
#        self.y = 0   #this will create the instance.x as 0
#
#p = Point()

class Point:
    """Point class to represent + manipulate x,y co ordinates"""
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def getX(self):
        return self.x
        
    def getY(self):
        return self.y
    
    def distanceFromOrigin(self): #you call self here to assign (p) later on as its given statements
        return((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def __str__(self):  #this allows to control what is printed out from the class when called with "print"
        return "x=" + str(self.x) + ", y=" + str(self.y)
    
    def halfway(self, target):
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my) # function allows to call upon another class using target then passing the other Point class instance
        
p = Point(3,4)
q = Point(5,12)
mid = p.halfway(q)

print(mid)
print(mid.getX())
print(mid.getY())   
    

#def distance(point1, point2):
#    xdiff = point2.getX() - point1.getX()
#    ydiff = point2.getY() - point1.getY()
#    
#    dist = math.sqrt(xdiff ** 2 + ydiff ** 2)
#    return dist

#p = Point(7,6) #good tip to remember - the P variable is what would be the "self" section
#print(p.getX())
#print(p.getY())
#print(p.distanceFromOrigin())

#p = Point(1,4)
#q = Point(5,5)
#print(distance(p,q))

