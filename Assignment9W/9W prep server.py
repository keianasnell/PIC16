#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 22:29:08 2017

@author: keianarei
"""

import socket

def Main():
    host = '127.0.0.1'
    port = 5000
    
    s = socket.socket()
    s.bind((host,port))
    s.listen(1)
    print "listening"
    c, addr = s.accept()
    print "connected socket made"
    print "Connection From: " + str(addr)
    
    
    while True: #true when connection established
        data = c.recv(1024)
        if not data:
            break
        print "From connected user:" + str(data)
        data = str(data).upper()
        print "Sending: " + str(data)
        c.send(data)
    
    c.close()
    
if __name__ == "__main__":
   Main()