# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 16:18:30 2017

@author: Callum
"""

#fruit = "apple"
#for idz in range(len(fruit)):
#    print(fruit[idz])




#fruit = "apple"
#
#position = 0
#while position < len(fruit):
#    print(fruit[position])
#    position = position + 1




#accumulator with strings
#def removeVowels(s):
#    vowels = "aeiouAEIOU"
#    sWithoutVowels = ""
#    for eachChar in s:
#        if eachChar not in vowels:
#            sWithoutVowels = sWithoutVowels + eachChar
#    return sWithoutVowels
#    
#print(removeVowels("compsci"))
#print(removeVowels("AaDfsdfoidvspodifrsdfAAAAIOuewsrOIOUSDF"))



#counting of a character within a given text
#def count(text, aChar):
#    lettercount = 0
#    for c in text:
#        if c == aChar:
#            lettercount = lettercount + 1
#    return lettercount
#
#print(count("banana","a"))

#The function count takes a string as its parameter. The for statement iterates through each character in the string and checks to see if the character is equal to the value of aChar. If so, the counting variable, lettercount, is incremented by one. When all characters have been processed, the lettercount is returned.



#Find function in finding and returning a specific index
#def find(astring, achar):
#    ix = 0
#    found = False
#    while ix < len(astring) and not found:
#        if astring[ix] == achar:
#            found = True
#        else:
#            ix = ix + 1
#    if found:
#        return ix
#    else:
#        return -1
#
#print(find("abcdefg", "a")) #will give 0 as its the first position


#count function tracking occurence of a letter in a text
#def count(x):
#    low = "abcdefghijklmnopqrstuvwxyz"
#    up = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
#    
#    e = 0
#    totalchar = 0
#    for achar in x:
#        if achar in low or achar in up:
#            totalchar = totalchar + 1
#            if achar == "e":
#                e = e + 1
#    print("this text has",totalchar,"characters, of which",e,"are the letter e")
#    
#print(count("There once was a man from peru, who thought he was eating his shoe"))
#            



#function to return number of digits in integer
#def numofdig(x):
#    x_str = str(x)
#    return len(x_str)
#
#print(numofdig(50))
#print(numofdig(100))
#print(numofdig(1000))



#list traversal
#fruit = ["apple","pear","banana","peach"]
#for afruit in fruit:      #by item ("apple","pear",etc)
#    print(afruit)



##indices used to iterate through the list of items
#fruit = ["apple","pear","banana","peach"]
#
#for position in range(len(fruit)):   #by index [0,1,2,3,etc]
#    print(fruit[position])
    

#printing multiples through a loop
#num = [1,2,3,4,5]
#print(num)
#
#for i in range(len(num)):   #i represents each value in the list[]
#    num[i] = num[i] ** 2
#print(num)

#function that doubles the value of an integer in a list + the list is mutable
#def double(aList):
#    for position in range(len(aList)):
#        aList[position] = 2 * aList[position]
#        
#a = [1,2,3,4]
#print(a)
#double(a)
#print(a)


##pure function (no side effects) of the double function above
#def double(aList):
#    new_List = []
#    for value in aList:
#        newElem = 2 * value
#        new_List.append(newElem)
#    return new_List
#
#a = [1,2,3,4]
#print(a)
#a = double(a)
#print(a)


#List comprehension
#mylist = [1,2,3,4,5]
#yourlist = [item  ** 2 for item in mylist]  # item = for each value in the mylist list
#print(yourlist)


#
##Simple nested list, using the reference to the index of the list item
#nested  = ["Hello",2.0, 5, [10,20]]
#innerlist = nested[3]   #selects the nested list
#print(innerlist)
#item = innerlist[1]     #selects 2nd position within the nested list
#print(item)
#
#print(nested[3][1])
#print(nested)
#
#


#song = "the rain in spain"
#wds = song.split("ai")   #giving a specific item to be removed from the string
#print(wds)


#
#wds = ["red","blue","green"]
#glue = ";"
#s = glue.join(wds)
#print(s)    #uses the delimiter of "glue" to join the strings together
#print(wds) #prints out the original list out 
#
#print("***".join(wds))   #uses the *** as a seperater (like glue uses ;)
#print("".join(wds))     # uses no whitespace to join together (resulting in one string)


#Using "list" as a type conversion from a string given value
#listedtype = list("Potato")
#print(listedtype)


#function that returns the circum + area of circle given the radius
#def circleinfo(r):
#    c = 2*3.14159*r
#    a = 3.14159*r*r
#    return(c,a)
#print(circleinfo(10))


#function that sums all the elements in a list up to but not including the first even number
#import random
#
#def sum(lst):
#    sum = 0
#    index = 0
#    while lst[index] % 2 != 0 and index < len(lst):
#        sum = sum + lst[index]
#        index = index + 1
#    return sum
#
#lst = []
#for i in range(100):
#    lst.append(random.randint(0,1000))
#print(sum(lst))



#simple list count function
#def count(obj, lst):
#    count = 0
#    for e in lst:
#        if e == obj:
#            count = count + 1
#    return count
#
#lst = [1,1,1,2,2,2,3,4,5,6]
#print(count(1, lst))



#open a file, then select a set of values inside
#A1 = open("A1.txt")
#
#for aline in A1:
#    values = aline.split()
#    print(values[0], values[1], values[3])
#A1.close()



#function thats recursive (solves each problem i.e the sum individually)
#def listsum(numlist):
#    if len(numlist) == 1:
#        return numlist[0]
#    else:
#        return numlist[0] + listsum(numlist[1:])
#print(listsum([1,2,3,4,5,6]))
























