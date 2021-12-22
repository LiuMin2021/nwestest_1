#!/usr/bin/env python3
# clientlein program

import socket

HOST = 'localhost'              # the remote host
PORT = 8080            # the save port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall( b'Hi BULME')
    data = s.recv(1024)
print('Received', repr(data))