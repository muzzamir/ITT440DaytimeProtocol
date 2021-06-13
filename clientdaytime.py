#client
import socket
import sys
from tqdm import tqdm , trange
import datetime
import time
from time import sleep
import os
#socket object
c = socket.socket()

#host port
host = "192.168.56.102"

port = 5050
#connection to the host port
try:
        print(f"Connecting to {host}:{port}")
except socket.error as e:
        print(str(e))

#Progress bar
pbar = tqdm(total=100)
for i in range(10):
    time.sleep(0.3)
    pbar.update(10)
pbar.close()
c.connect((host, port))
print("Connected")
time.sleep(1)

#output
def fmenu():
        print("Welcome, please enter 1 to continue")
        opt = input("")

        return opt
#menu
def Datetime():
        print("Please choose below:")
        print("Enter 1 to see date and time")
        print("Enter 0 to exit the program")
        sel = input("Please select your choice :")

        return sel
#Main
os.system('clear')
while True:
        opt = fmenu()
        loop = 1
        while loop == 1:
                if opt == '1':
                        os.system('clear')
                        sel = Datetime()
                        if sel == '1':
                                os.system('clear')
                                c.send(sel.encode())
                                tm = c.recv(38)
                                print("Time and date is %s" % tm.decode('utf-8'))
                                a = input("Please enter 1 to go back, enter 0 to exit")
                                if a == '1':
                                        loop = 1
                                else:
                                        sys.exit()
                        elif sel == '0':
                                print("Exit the system")
                                sys.exit()
                else:
                        print("exit")
                        sys.exit()
                        clientsocket.close()
        print("Exit the system")
c.close()
