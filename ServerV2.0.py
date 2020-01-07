import time
import socket
import sys


print("Welcome to AVIAN Help Center Version 2.0!")
print("")
print("Initializing...")
#Do 'time.sleep(number of seconds)' so that the execution of a program delays for a few seconds
time.sleep(1)


soc=socket.socket()
HOST=socket.gethostname()
PORT=8080
soc.bind((HOST,PORT))
print("")
print("NAME OF HOST SERVER:","",HOST)
print("")
name=input(str("Please enter your username:"))
soc.listen(5)
print("")
print("Waiting for any incoming connections...")
print("")
conn,addr=soc.accept()
print("CONNECTION RECEIVED")

sender_name=conn.recv(1024)
sender_name=sender_name.decode()
print("")
print(sender_name,"has entered the room and needs help!")
print("")
conn.send(name.encode())



##Make a loop so that the server can continuously SEND messages##

while True:
    message=input(str(">> :"))
    message=message.encode()
    conn.send(message)
    print(u'\u2713')
    print("")
    message=conn.recv(1024)
    message=message.decode()
    print("")
    print(sender_name,":",message)
    print("")







