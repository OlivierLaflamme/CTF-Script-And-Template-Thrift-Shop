#!/usr/bin/env python

import socket
import re

def answer(s, data="0\n"):
  s.send(data)
  s.recv(1000)

TCP_IP = ''
TCP_PORT = 0
BUFFER_SIZE = 1024
DATA = ""

def connect(TCP_IP, TCP_PORT):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((TCP_IP, TCP_PORT))
  return s

s = connect(TCP_IP, TCP_PORT)

s.send(DATA+"\n")
print s.recv(BUFFER_SIZE)

s.close()
