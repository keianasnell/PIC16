#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 13:54:41 2017

@author: keianarei
"""


class MathVector:
    def __init__(self, n, *args):
        self.vec = []
        if len(args)==0:
            if isinstance(n, list):
                self.vec = n
            else:
                for num in range(n):
                    self.vec.append(0)
        else:
            self.vec.append(n)
            for num in args:
                self.vec.append(num)


    def get_el(self, index):
        #returns the i-th component of the vector(1-indexed)
        #NOT zero-indexed
        return self.vec[index-1]
    
    def neg(self):
        #returns the negative of the original 
        #vector(leaving the original unchanged)
        return MathVector([num*(-1) for num in self.vec])

        #use generator expression
    def mag(self,):
        #returns the magnitude of the vector
        #square each value, add them, and take square root
        return (sum((self.vec[i]**2) for i in range(len(self.vec))))**0.5
    
    #use generator expression
    def dot(self, vec2):
        #returns the dot product of the vector and another vector
        return sum((self.vec[i]*vec2.get_el(i+1)) for i in range(len(self.vec)))
    
    def plus(self,vec2):
        #returns the sum of the vector and another vector
        return MathVector([(self.vec[i] + vec2.get_el(i+1)) for i in range(len(self.vec))])    
    
    def sp(self, scalar):
        #returns the product of the vector and a scalar
        return MathVector([(num*scalar) for num in self.vec])
    
    def print_me(self):
        #prints a representation of the vector
        #to the console like “[1, 0, 0]”
        print self.vec
        
    #~~~MAGIC METHODS~~~    
         
    def __str__(self):
        return str(self.vec)
       
     #bracket notation
    def __getitem__(self, index):
        return self.vec[index-1]
    
     #negation
    def __neg__(self):
        return MathVector([num*(-1) for num in self.vec])
    
     #abs = magnitude
    def __abs__(self):
        return (sum((self.vec[i]**2) for i in range(len(self.vec))))**0.5
         
     #multiplication -after
    def __mul__(self, other):
        if isinstance(other, int):
            return MathVector([(num*other) for num in self.vec])
        else:
            return sum((self.vec[i]*other.get_el(i+1)) for i in range(len(self.vec)))
    #multiplication -before
    def __rmul__(self, other):
        return MathVector([(num*other) for num in self.vec])         
        
     #addition
    def __add__(self, other):
        return MathVector([(self.vec[i] + other.get_el(i+1)) for i in range(len(self.vec))])


#TEST CODE
u = MathVector(5)
print "u =",
u.print_me()
 
v = MathVector([2,3,6])
print "v =",
v.print_me()
 
w = MathVector(1,2,3)
print "w =",
w.print_me()

print v.get_el(2)
v.neg().print_me()
print v.mag()
print v.dot(w)
v.plus(w).print_me()
v.sp(3).print_me()

print v
print v[2]
print -v
print abs(v)
print v*w
print v+w
print v*3
print 3*v