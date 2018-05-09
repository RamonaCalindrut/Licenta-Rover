# -*- coding: utf-8 -*-
"""
Created on Tue May  8 18:29:52 2018

@author: patrick.schmiedt
"""

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="192.168.43.237"
port =3000
s.connect((host,port))

def ts(str):
   s.send(str.encode()) 
   data = ''
   data = s.recv(1024).decode()
   print (data)

while 2:
   r = input('Enter a string: ')
   ts(r)

s.close ()