#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 12:12:59 2017

@author: keianarei
"""
from __future__ import division
import nltk
from nltk import word_tokenize
from nltk import FreqDist, WordNetLemmatizer, Text
from urllib import urlopen
from nltk.corpus import wordnet
from nltk.wsd import lesk


def lexical_diversity(x, y):
    return len(x)/len(y)

#2--open the plain text
url = "https://www.gutenberg.org/files/863/863-0.txt"
response =  urlopen(url)
raw = response.read().decode('utf8')

#3--edit the raw data
x = raw.find("CHAPTER I. I GO TO STYLES")
y= raw.rfind("THE END")
raw = raw[x:y]

#4--using code from Assignment 1F (dictionary)
list1 = raw.split()
b = {}
for word in list1:
    if word not in b:
        b[word] = 1
    else:
        b[word] += 1

lexical_div1 = len(set(list1))/len(list1)
print lexical_div1 #0.176525804966

#4--using FreqDist instead 
list2 = raw.split()
fdist1 = FreqDist(list2)
lexical_div1 =  lexical_diversity(fdist1, list2)	
print lexical_div1

#5--rid original texts of underscores
raw2 = ""
for char in raw:
    if char == "_":
        char = ""
        raw2 += char
    else:
        raw2 += char
        
list3 = word_tokenize(raw2)
fdist2 = FreqDist(list3)
lexical_div3 = len(fdist2)/len(list3)
print lexical_div3 #0.0802709126128

#10--print out 30 most used words
print fdist2.most_common(30)

##11--print out 30 most used words that begin with a letter
most_common = {word:fdist2[word] for word in fdist2 if word.isalpha()}
most_common = sorted(most_common.items(), key=lambda x:x[1], reverse=True)
print most_common[:30]

#6--eliminate words distinct only in letter pass
for word in fdist2:
    for word2 in fdist2:
        if word != word2:
            if word.lower() == word2.lower():
                fdist2[word] = fdist2[word] + fdist2[word2]
                fdist2[word2] = 0
                
for word in fdist2.items():
    if fdist2[word]==0:
        fdist2.__delitem__(word)
 
#7--eliminate words distinct only in affixes
porter = nltk.PorterStemmer()
no_affix = {porter.stem(word): fdist2[word] for word in fdist2}
print no_affix

#8--convert into nltk.Text object
text = Text(list3)
print text.concordance('point') #23 matches


#9--WordNet synsets
#part a
for ss in wordnet.synsets('point'):
    print(ss, ss.definition())
#part b
sents = nltk.sent_tokenize(raw)
point_sents = []
for sentence in sents:
    if ' point ' in sentence:
        point_sents.append(sentence)
        print sentence
#part c
for sentence in point_sents:
   print (lesk(sentence, 'point'))
#part d
for sentence in point_sents:
   print (lesk(sentence, 'point', pos='n'))
