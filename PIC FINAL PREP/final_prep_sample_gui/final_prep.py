#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 11:58:51 2017

@author: keianarei
"""

f = open('/Users/keianarei/Desktop/PIC16/PIC FINAL PREP/PIC 16 Exam Practice/heights.csv', 'r')
f.readline()

dict = {}
for x in f:
    for char in x:
        if char==',':
            y = x[0:x.index(char)]
            z = x[x.index(char)+1:]
            z = float(z)
            dict[y] = z

def gen(dict):
    #gotta get the height from here
    
#calculate average height

#f = open('/Users/keianarei/Desktop/PIC16/PIC FINAL PREP/PIC 16 Exam Practice/words.txt', 'r')
#
#words = []
#y = 0
#for line in f:
#    for char in line:
#        if char.isspace():
#           y = line.split(char)
#           words.append(y)
#print words