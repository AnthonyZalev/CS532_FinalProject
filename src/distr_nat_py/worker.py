#!/usr/bin/env python3
import socket
import sys

print(sys.argv)

num_servers = 1

s = socket.socket()
host = socket.gethostname()  # Get local machine name
print(host)
port = int(sys.argv[1])  # Reserve a port for your service
s.bind((host, port))  # Bind to the port

s.listen(5)  # Now wait for client connection
while True:
    c, addr = s.accept()  # Establish connection with client
    print("Connection from", addr, "has been established.")
    l = c.recv(4)
    print("Reading",l,"bytes")

    l = c.recv(1024)
    word_count = len(l.split())
    while l:
        l = c.recv(1024)
        word_count += len(l.split())
    print "Done Receiving"
    c.send(str(word_count))
    c.close()                # Close the connection
