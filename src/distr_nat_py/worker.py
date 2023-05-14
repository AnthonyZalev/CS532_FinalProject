#!/usr/bin/env python3
import socket
import sys

FILE_PREFIX = 'shakespeare_processed_'

num_servers = 1

s = socket.socket()
host = socket.gethostname()  # Get local machine name
print(host)
port = int(sys.argv[1])  # Reserve a port for your service
num = sys.argv[2]
s.bind((host, port))  # Bind to the port

s.listen(5)  # Now wait for client connection
while True:
    c, addr = s.accept()  # Establish connection with client
    # receiving all data at once
    data = c.recv(2048)
    args = data.split()

    # Which file we are using
    file_no = int(args[0])
    file_name = FILE_PREFIX+str(file_no)+'_'+num+'.txt'

    # Size of the chunk the server is processing
    num_lines = int(args[1])
    num_lines = int(num_lines)

    # Starting position
    starting_pos = int(args[2])
    starting_pos = int(starting_pos)

    # TODO: change the code below to read a particular file...
    with open(file_name) as f:
        f.seek(starting_pos, 0)
        data = f.read(num_lines)
    
    word_count = len(data.split())
    c.send(str(word_count))
    c.close()                # Close the connection