#!/usr/bin/env python3
# nwestest1: serverlein program

import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 8080               # Arbitrary non-privileged port
#encode = (UTF-8)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    while True:
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024) 
                if not data: break
                outdata = data[::-1]      #reverse data: hello->olleh
                print('Hi BULME')
                conn.sendall(outdata)
                
                conn.close()
