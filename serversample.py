#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 16:38:19 2017

@author: keianarei
"""

import socket
import threading

#class Server:
#    self.sock = socket.socket()
#    def __init__(self):
#        self.sock.bind(('0.0.0.0', 5000))
#        self.sock.listen(1)
#    
#    connections = []
#    
#    def handler(self, c, addr):
#        while True:
#            data = c.recv(1024)
#            for connection in self.connections:
#                connection.send(data)
#            if not data:
#                break
#    while True:
#        c, addr = self.sock.accept()
#        connections.append(c)
#        print(connections)
#        
sock = socket.socket()
host = '0.0.0.0'
port = 10000
sock.bind((host, port))
sock.listen(1)

connections = []

def handler(self, c, addr):
    global connections
    while True:
        data = c.recv(1024)
        for connection in connections:
            connection.send(bytes(data))
        if not data:
            connections.remove(c)
            c.close()
            break

while True:
    c, addr = sock.accept()
    cThread = threading.Thread(target=handler, args=(c,addr))
    cThread.daemon = True
    cThread.start()
    connections.append(c)
    print(connections)