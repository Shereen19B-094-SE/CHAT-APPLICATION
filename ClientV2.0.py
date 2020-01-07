import time
import socket
import sys
from tkinter import*
#Do same initialization method as V 1.0

print("Welcome to AVIAN Help Center Version 2.0!")
print("")
print("Initializing...")
#Do 'time.sleep(number of seconds)' so that the execution of a program delays for a few seconds
time.sleep(1)
print("Name of the available host server is.....LAPTOP-9D19D51H")
s=socket.socket()
print("")
HOST=input(str("Please enter the host server's address/name:"))
print("")
NAME=input(str("Please enter your name:"))
print("")
PORT=8080
print("Trying to connect to",HOST," at port",PORT,"...")
print("")
#Add execution delay of 1 second
time.sleep(1)
s.connect((HOST,PORT))
print("CONNECTED TO HELP CENTER")
print("")
####connection done###

#Make a code for the client's username feature. This one will allow the CLIENT to SEND their username to the host#
##Convert the username from bytes to bits using 'name.encode()'##
##Also make a code for the client to RECEIVE the username of the HOST
s.send(NAME.encode())
s_name=s.recv(1024)
s_name=s_name.decode()
print(s_name,"has entered the room and will assist you!")

#Create a loop so that the client may continuously receive messages
def receive():
    while True:
        message=s.recv(1024)
        message=message.decode()
        print("")
        print(s_name,":",message)
        print("")

def send(event=None):
    message=my_msg.get()
    my_msg.set("")
    message=input(str("You:"))
    message=message.encode()
    s.send(message)
    print(u'\u2713')
    print("")

def on_closing(event=None):
    my_msg.set("{quit}")
    send()

top=Tk()
top.title("AVIAN")

messages_frame=Frame(top)
my_msg=StringVar()
my_msg.set("Type your messages here")

scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = tkinter.Entry(top, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()
send_button = tkinter.Button(top, text="Send", command=send)
send_button.pack()

top.protocol("WM_DELETE_WINDOW", on_closing)
