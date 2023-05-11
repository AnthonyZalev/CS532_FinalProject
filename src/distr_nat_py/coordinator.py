#!/usr/bin/env python3
import socket
from sys import getsizeof
from threading import Thread
import os, time


NUM_WORKERS = 6
HOST = host = 'elnux2.cs.umass.edu' # Change this depending on server
port = 12345                        # Specify the port to connect to
WORKER_PORTS = [12344, 12345, 12346, 12347, 12348, 12349]       # Scale this to number of workers  
thread_list = []
word_count_total = 0
CHUNK_SIZE = 2048

# Code From: https://coderslegacy.com/python/get-return-value-from-thread/
class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)      
    def join(self, *args):
        Thread.join(self, *args)
        return self._return


def send_and_recv_thread(num, port_num, file, num_workers):
    # Connecting Socket
    s = socket.socket()
    s.connect((host, port_num))  
    # Sending file over
    f = open(file, 'rb')
    # Sending the file in specific chunks
    file_size = os.path.getsize(file)
    bytes_to_send = int(file_size/num_workers)
    # Telling the server the size of the chunk:
    s.send(str(bytes_to_send).encode('utf-8'))
    starting_pos = bytes_to_send*num
    f.seek(starting_pos, 0)
    bytes_left = bytes_to_send
    while bytes_left > 0:
        if bytes_left >= CHUNK_SIZE:
            l = f.read(CHUNK_SIZE)
            bytes_left -= CHUNK_SIZE
        else:
            l = f.read(bytes_left)
            bytes_left = 0
        s.send(l)
    f.close()
    s.shutdown(socket.SHUT_WR)
    thread_wc = s.recv(1024)
    s.close()  # Close the socket when done
    return thread_wc

files = ["C:/Users/MZambetti1/Documents/CS 677/Lab 3/CS532_FinalProject/src/data/shakespeare_processed_2048.txt"]
#         "C:/Users/MZambetti1/Documents/CS 677/Lab 3/CS532_FinalProject/src/data/shakespeare_processed_16.txt",
#         "C:/Users/MZambetti1/Documents/CS 677/Lab 3/CS532_FinalProject/src/data/shakespeare_processed_64.txt",
#         "C:/Users/MZambetti1/Documents/CS 677/Lab 3/CS532_FinalProject/src/data/shakespeare_processed_256.txt",
#         "C:/Users/MZambetti1/Documents/CS 677/Lab 3/CS532_FinalProject/src/data/shakespeare_processed_1024.txt",
#         "C:/Users/MZambetti1/Documents/CS 677/Lab 3/CS532_FinalProject/src/data/shakespeare_processed_2048.txt",]

for file in files:
    start_time = time.time()
    for worker_idx in range(NUM_WORKERS):
        tx = CustomThread(target=send_and_recv_thread,args=(worker_idx, 
                                WORKER_PORTS[worker_idx], 
                                file,
                                NUM_WORKERS))
        tx.start()
        thread_list.append(tx)
        # Need to spawn a thread to send and recieve the data
        pass

    for idx in range(NUM_WORKERS):
        word_count_total += int(thread_list[idx].join())
    print()
    print(file)
    print("Time taken:", time.time()-start_time)
    print("Final word count=",word_count_total)

