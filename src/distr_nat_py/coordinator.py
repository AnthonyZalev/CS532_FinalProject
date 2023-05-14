#!/usr/bin/env python3
import socket
from sys import getsizeof
from threading import Thread
import os, time


NUM_WORKERS = 2
HOST = host = 'elnux3.cs.umass.edu' # Change this depending on server
port = 12345                        # Specify the port to connect to
WORKER_PORTS = [12340, 12341, 12342, 12343, 12344, 12345]       # Scale this to number of workers  
thread_list = []
word_count_total = 0
CHUNK_SIZE = 2048
FILE_PREFIX = 'C:/Users/MZambetti1/Documents/CS 677/Lab 3/CS532_FinalProject/src/data/shakespeare_processed_'

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


def send_and_recv_thread(num, port_num, file_no, num_workers):
    # Connecting Socket
    s = socket.socket()
    s.connect((host, port_num))  

    # Need to tell the server which file we are using
    file_no = str(file_no)
    #s.send(val)

    # Sending the file in specific chunks
    file_size = os.path.getsize(FILE_PREFIX+str(file_no)+'.txt')
    bytes_to_send = int(file_size/num_workers)
    
    # Telling the server the size of the chunk:
    starting_pos = bytes_to_send*num
    bytes_to_send = str(bytes_to_send)

    # Also need to send the starting position over
    starting_pos = str(starting_pos)

    # Once peer recieves this number they should start
    data = file_no+' '+bytes_to_send+' '+starting_pos
    s.send(data.encode())

    thread_wc = s.recv(2048)
    s.close()  # Close the socket when done
    return thread_wc

file_numbers = [1, 16, 64, 256, 1024, 2048]

file_no = file_numbers[4]
start_time = time.time()
for worker_idx in range(NUM_WORKERS):
    tx = CustomThread(target=send_and_recv_thread,args=(worker_idx, 
                            WORKER_PORTS[worker_idx], 
                            file_no,
                            NUM_WORKERS))
    tx.start()
    thread_list.append(tx)

for idx in range(NUM_WORKERS):
    word_count_total += int(thread_list[idx].join())
print("Time taken:", time.time()-start_time)
print("Final word count=",word_count_total)

