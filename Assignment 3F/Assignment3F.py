#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:39:15 2017

@author: keianarei
"""

import re
import csv


with open('data.csv', 'r') as f:
    a = csv.reader(f)
    a.next()
    
    determine_name = r"^\w+\,"
    name_regex1 = r"(\w+)\,\s(\w+)\s?([A-Z]?\.?)"
    name_regex2 = r"(\w+)\s?([A-Z]?\.?)\s(\w+)"
    phone_regex = r"1?\W?\(?(\d{3})\)?\s?\W?(\d{3})\s?\W?(\w{4})"
    
    g = open('data2.csv', 'w')
    z = csv.writer(g)
    z.writerow(["First", "M.I.", "Last", "Number"])
            
    for row in a:
        x = re.findall(determine_name, row[0])
        if len(x)!=0:
            name = re.findall(name_regex1, row[0])
        else:
            name = re.findall(name_regex2, row[0])
            
        first, middle, last = name[0]
        if len(middle)!=2:
            if len(middle)==0:
                pass
            elif len(last)==2:
                temp = first
                first = middle
                middle = last
                last = temp
            elif len(last)==0:
                last, middle = middle, last
                first, last = last, first
        
        y = re.findall(phone_regex, row[1])
        if(len(y)==1):
            j, k, l = y[0]
            num = "(" + j + ") " + k + "-" + l
            z.writerow([first, middle, last, num])

    g.close()

