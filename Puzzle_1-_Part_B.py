from threading import Thread
from socket import *
import os
import time
import random

even = [0.06,0.04,0.04,0.04,0.06,0.06]
odd = [0.3,0.3,0.1,0.3,0.1,0.1]
notDefined = True

def create_socket(server_port):
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_socket.bind(('', server_port))
    server_socket.listen(1)
    return server_socket

def accept_client(server_socket):
    connection_socket, address = server_socket.accept()
    return connection_socket, address 

#send message to client
def send_message(connection_socket, message):
    connection_socket.send(message)
    return

def callbackFunction(connection_socket,address,mesg):
    n = 0
    covert_bin = ""
    #convert covert message to binary value
    for msg in covert_msg:
        covert_bin += format(ord(msg),'#010b')[2:]
    #print(covert_bin)
    #send covert message with time gap based on the 1 or 0 value
    for msg in Msg:        
        send_message(connection_socket, msg.encode())
        rand = int(random.uniform(0,5))
        if covert_bin[n] == "0":
            time.sleep(even[rand])
        else:
            time.sleep(odd[rand])
        n = (n+1)%len(covert_bin)
    send_message(connection_socket, "EOF".encode())
    connection_socket.close()


server_port = 12003
server_socket = create_socket(int(server_port))
print("The server is ready to receive \n")

if notDefined:
    covert_msg = "You have escaped the first gate. Now, Connect to SSH server on III.JJJ.KKK.LLL port ABCD, user: \"billythekid\",pass: \"PatGarret\". Be careful with wrong doors. You will be trapped."
    Msg = "Once one of the top 15 fugitives wanted by the United States’ Marshals, Richard Lee McNair is currently serving a sentence for two terms of life imprisonment in Florence, Colorado. \
    After being caught when he escaped from prison the first two times, McNair etched out a plan for his third escape. \
    McNair was imprisoned at a United States Penitentiary in Pollock, Louisiana. His prison duties involved mending the old and torn mailbags in the manufacturing area. \
    In several months that followed, as he did this work, he plotted his escape. \
    He built himself an escape pod that had a breathing tube in it. \
    He climbed into the pod and patiently waited for over an hour in it until the crate was forklifted to a warehouse that was outside the prison fence. \
    When the guards at warehouse left for lunch, he cut himself out of the crate and escaped on April 5, 2006. \
    He got into the create at 9:45 am and got out of it at 11:00 am. He knew that no one would notice he was missing until 4:00 pm.\
    Hours after that, he was stopped by a police officer when he was seen running near a railroad track in Ball, Louisiana. \
    McNair laughed and joked with the officer and conviced him he was a jogger from out of the town. \
    All of this was captured on Bordelon’s patrolling camera, and Bordelon already knew about the escape of a prisoner \
    but wasn’t given an accurate description or a new photograph.THE END..."
while(1):
    connection_socket, address = accept_client(server_socket)

    t1 = Thread(target=callbackFunction,args=(connection_socket,address,Msg,)).start()
    
    zero = 0.025
    one = 0.1
    
    #time.sleep(one)
