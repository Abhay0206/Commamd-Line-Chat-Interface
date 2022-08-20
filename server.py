import socket
import random
import datetime
from _thread import *

# Creating the socket
try:
    print("Creating the Socket....")
    s = socket.socket()
    print("Socket created successfully.")
except socket.error as err:
    print("Socket creation failed due to " + str(err))

#defining host
host = socket.gethostname()
print("Host: ", host)

#defining port
port = 80

ThreadCount = 0

def dt():
    now = datetime.datetime.now()
    return(now.strftime("%Y-%m-%d %H:%M:%S"))

try:
    print("Binding the Socket....")
    s.bind((host, port))
    print("Socket binded successfully.")
except socket.error as err:
    print("There is some problem resolving the host " + str(err))
    quit()

print('Waitiing for a Connection..')
s.listen(100)

def threaded_client(c):
    message = "Welcome to the Server."
    message = message.encode('utf-8')
    c.send(message)
    while True:
        incoming_message = c.recv(1024)
        incoming_message = incoming_message.decode('utf-8')
        if len(str(incoming_message)) > 0:
            print(dt())
            print("Client " + "(" + address[0] + ":" + str(address[1]) + ")" + ": " +  incoming_message)
            print("message received")
        else:
            break
        sending_message = input("You: ")
        sending_message = sending_message.encode('utf-8')
        c.send(sending_message)
        print("message sent")
    c.close()

while True:
    c, address = s.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (c, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
s.close()