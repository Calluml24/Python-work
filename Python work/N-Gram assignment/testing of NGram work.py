# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 09:58:49 2017

@author: Callum
"""


#Callum Lucking - w7i78
#N-Gram Assignment 

#The below program has been created to run 2 sets of texts by 2 different authors, create N-Grams of "n" length, generate the top 20 occurring 
#N-Grams and then calculate the mean and standard deviation of both sets.

#Some issues i had to deal with during this design: 
#Firstly, working out a logical and sensible way for going through the stages of production and ensuring it flows well and not overly complex
#Secondly, i struggled early on with effectively opening the files and being able to carry those newly generated lists over into the next sections
#Finally, i found it hard early on to decide whether i needed to create a function for a process or not, and then being able to generate a variable that i could 
#call upon later rather than having the output simply be sat as an output that cannot be used in other parts further down.

#used this to import the numpy to allow calculations of the mean + standard deviation of both lists
import numpy as npy

#Global variables for indvA+B to allow it too be called by other functions
indvA = []
indvB = []

#function that runs the text file as read and then splits into individual words
def readFileA(file):
    global indvA      #Had issues here with trying to access this list outside of the function to be called upon
    with open(file, 'r') as f:
        for line in f:
            indvA += line.split()
        return indvA

#print(indvA)

#combining all 6 author A text files together to be run through the program below. I thought a logical step would be to combine all texts to simplify the 
#process of getting the Ngram list
Auth_A = ["A1.txt","A2.txt","A3.txt","A4.txt","A5.txt","A6.txt"]
with open('Auth_A.txt', 'w') as outfile:   #using this instead of a pure file open so that i do not need to close it afterwards
    for file_name in Auth_A:
        with open(file_name) as infile:
            for line in infile:
                outfile.write(line)

#I had to create this variable that runs the readFile function given the full texts, too allow the variable to passed forward in the program
new_listA = readFileA("Auth_A.txt")

#print(new_listA)    #had this placed through the program to allow for some sanity checking as a went through. ensuring all work was carrying forward correctly

#this takes the full list and breaks it up using list comprehension too obtain 3 word long lists that iterate through the text 1 value at a time. (ie - a,b,c | b,c,d)
#i took this approach as it keeps things simple as well as being able to change the length of the split
split_list = [new_listA[x:x+3] for x in range(0, len(new_listA),1)]

#take this split list and add a counter too it, also pushed the split_list above into a tupled dictionary to allow for the counter (value) to go alongside the split_list(key)
nGram_counterA = {}
for i in split_list:
    i = str(i)
    if i in nGram_counterA:
        nGram_counterA[i] += 1
    else:
        nGram_counterA[i] = 1

#take the dictionary and sort it by frequency using the itemgetter module, this sorts the dictionary out by value,key pair with the counter on the value        
from operator import itemgetter   
sorted(nGram_counterA.items(), key = itemgetter(1))

#variable created that 
nGram_listA = nGram_counterA

#Pass the dictionary(counter) through a function/ program that only brings up the top 20 most frequent occurring Ngrams
from collections import OrderedDict  #used this here to only bring in the OrderedDict function to save memory on calling in the whole library
def top_20_nGramA(file, n, order = True): #Went with a function here as i wanted to be able to pass through "n", rather than including a specific integer that cannot be changed
        top = sorted(file.items(), key = lambda x: x[1], reverse = True)[:n] #referenced through using indexing to select the value
        if order:
            return OrderedDict(top)
        return dict(top)

#Once again, including this line to allow for a single named variable to be called upon later on
AuthA_final = top_20_nGramA(nGram_listA, 20)

#.....................................................................................................................................................................
#Re-run of above but for Author B - see above commentary which would be reflected with the below

def readFileB(file):
    global indvB
    with open(file, 'r') as f:
        for line in f:
            indvB += line.split()
        return indvB
   
Auth_B = ["B1.txt","B2.txt","B3.txt","B4.txt","B5.txt","B6.txt"]
with open('Auth_B.txt', 'w') as outfile:
    for file_name in Auth_B:
        with open(file_name) as infile:
            for line in infile:
                outfile.write(line)

new_listB = readFileB("Auth_B.txt")

split_list = [new_listB[x:x+3] for x in range(0, len(new_listB),1)]

nGram_counterB = {}
for i in split_list:
    i = str(i)
    if i in nGram_counterB:
        nGram_counterB[i] += 1
    else:
        nGram_counterB[i] = 1

from operator import itemgetter
sorted(nGram_counterB.items(), key = itemgetter(1))

nGram_listB = nGram_counterB

def top_20_nGramB(file, n, order = True):
        top = sorted(file.items(), key = lambda x: x[1], reverse = True)[:n]
        if order:
            return OrderedDict(top)
        return dict(top)

AuthB_final = top_20_nGramB(nGram_listB, 20)
print("")  #included these to help seperate the individual prints in the console, for ease of reading
print("Author A top 20 N-Grams: ", AuthA_final)
print("")
print("Author B top 20 N-Grams: ", AuthB_final)
print("")  

#convert the values in dictionary to a list to allow for ease of calculation of the values only
t20_list_A = list(AuthA_final.values())

#calculate the mean and standard deviation for both the above 20 from the original full list (using the numpy library)

#Mean for Author A
print("The mean of the top 20 N-Grams for Author A is: ", (npy.mean(t20_list_A)))
print("")
#Standard deviation of Author A
print("The standard deviation of the top 20 N-Grams for Author A is: ", (npy.std(t20_list_A)))
print("")
#Repeated for Author B
t20_list_B = list(AuthB_final.values())
print("The mean of the top 20 N-Grams for Author B is: ", (npy.mean(t20_list_B)))
print("")
print("The standard deviation of the top 20 N-Grams for Author A is: ", (npy.std(t20_list_B)))
print("")


