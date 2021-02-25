import random
lis = []
#get alphabets and numbers in a list
for i in range(0,26):
    lis.append(chr(97+i))
for i in range(0,26):
    lis.append(chr(65+i))
for i in range(0,9):
    lis.append(chr(49+i))
lis.append('0')

header =  "The credentials for TCP server are encrypted using a new pattern/method by nerd jailer and to decrypt it many prisoners tried but failed. \nOnly 4 prison escapees got success in decoding it. One of them left a clue i.e.., each character represents either 0 or 1. Get least significant bits (LSB) in binary ASCII value of each character and combined value is the key to this Puzzle."
msg = "The key is embedded in a timing covert channel. Connect to server with ip address aaa.bbb.ccc.ddd with port number IJKLM. Decode the covert message. Hurry up! Guards may wakeup anytime! ....... By the way, You'll have to answer 3 riddles in the begining. Prepare to \'client_socket.recv(2048)\' and \'client.socket.send()\' three times (for loop)"

#get ASCII value of each character in the message
lis2=""
for i in msg:
    lis2+=format(ord(i),'07b')

#generate binary value of each ASCII value and generate a random character based on the odd or even status of binary ASCII value
encodedMsg = ""
for i in lis2:
    temp = int(random.random() * 60)
    if int(i) == 1:
        if temp%2 == 1:
            temp+=1
    else:
        if temp%2 == 0:
            temp+=1
    encodedMsg+= lis[temp]

file = open('Puzzle_0.txt', 'w+')
file.writelines([header,"\n\nEncrypted Message:\n",encodedMsg])
file.close()

