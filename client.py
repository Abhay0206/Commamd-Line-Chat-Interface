import socket
import datetime
import random
# Creating the socket
try:
    print("Creating the Socket....")
    s = socket.socket()
    print("Socket created successfully.")
except socket.error as err:
    print("Socket creation failed due to " + str(err))

#Copy the host from the terminal of server.py file.
host = input("Enter the host name: ")

port = 80

def dt():
    now = datetime.datetime.now()
    return(now.strftime("%Y-%m-%d %H:%M:%S"))

print('Waiting for connection')
try:
    s.connect((host, port))
    print("Socket is conncted with the server.")
except socket.error as err:
    print("There is some problem in resolving the host " + str(err))

incoming_message = s.recv(1024)
incoming_message = incoming_message.decode('utf-8')
print("Server: ", incoming_message)
while True:
    ts = input('Do you want to continue[y/n]: ')
    if ts == 'y':
        sending_message = input("You: ")
        sending_message = sending_message.encode('utf-8')
        s.send(sending_message)
        print("message sent")
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode('utf-8')
        print(dt())
        print("Server: ", incoming_message)
        print("message received")
    else:
        break

s.close()