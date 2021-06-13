#server
import socket
import time
import datetime
import tqdm
from time import sleep
import sys
from datetime import timedelta
import os
from _thread import *
#socket object
s = socket.socket()

#display
def typingPrint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)


def close():
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        print("Server close")

typingPrint("Socket successfully created\n")
#gethostname
host = socket.gethostname()
port = 5050
ThreadCount = 0
#binding
s.bind(('',port))
typingPrint("Socket is binded to "+str(port)+"\n")
#listen
s.listen(5)
typingPrint("Socket is listening\n")
#Waiting connection from client
typingPrint("Socket is waiting connection from client\n")
def threaded_client(connection):
        typingPrint("Connection Successful \n")
        while True:
                sel = connection.recv(1024).decode('utf-8')
                if sel == '1':
                        ctime=datetime.datetime.now().strftime('%A %d %B %Y %H:%M:%S %p')
                        connection.send(str(ctime).encode())
                elif sel == '0':
                        close()
        connection.close()
#Main
while True:
        client,addr = s.accept()
        print('Connected to :'+addr[0]+':'+str(addr[1]))
        start_new_thread(threaded_client,(client,))
        ThreadCount += 1
        print('Thread Number:' + str(ThreadCount))
s.close()
