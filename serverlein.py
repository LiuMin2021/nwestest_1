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
                outdata = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"
                antwort = "HTTP/1.1 200 OK\r\n\r\n<html><body><h1>Hi BULME</h1></body></html>" #reverse data: hello->olleh
                
                conn.sendall(antwort)
                
                conn.close()
