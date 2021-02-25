import random
lis = []
for i in range(0,26):
    lis.append(chr(97+i))
for i in range(0,26):
    lis.append(chr(65+i))
for i in range(0,9):
    lis.append(chr(49+i))
lis.append('0')
#print(lis)
msg = "The key is embedded in a timing covert channel. Connect to server with ip address aaa.bbb.ccc.ddd with port number IJKLM. Decode the covert message. Hurry up! Guards may wakeup anytime"
msg2 = "USE VIGENERE CIPHER TO DECRYPT THE NEXT PART with challenge name as KEY- NFC EIFU CIABC KW VSNM NMTR IYM GRQ BEH EFTE QF ZVGV. ES GTCT SG VO WMGEGVA - YSBSXI EVXFB"
lis2=""
for i in msg:
    lis2+=format(ord(i),'07b')
'''
lis3 = ""
for j in range(0,len(lis2),7):
    lis3+= chr(int(lis2[j:j+7],2))
'''

encodedMsg = ""
for i in lis2:
    temp = int(random.random() * 60)
    if int(i) == 1:
        if temp%2 == 1:
            temp+=1
    else:
        if temp%2 == 0:
            temp+=1
    #print(i,temp,ord(lis[temp]),lis[temp])
    encodedMsg+= lis[temp]
print(encodedMsg)

lis4=""
for i in encodedMsg:
    lis4+= str(ord(i)%2)

lis3 = ""
for j in range(0,len(lis4),7):
    lis3+= chr(int(lis4[j:j+7],2))
print(lis3)

lis2=""
for i in msg2:
    lis2+=format(ord(i),'07b')

encodedMsg = ""
for i in lis2:
    temp = int(random.random() * 60)
    if int(i) == 1:
        if temp%2 == 1:
            temp+=1
    else:
        if temp%2 == 0:
            temp+=1
    #print(i,temp,ord(lis[temp]),lis[temp])
    encodedMsg+= lis[temp]
print(encodedMsg)

lis4=""
for i in encodedMsg:
    lis4+= str(ord(i)%2)

lis3 = ""
for j in range(0,len(lis4),7):
    lis3+= chr(int(lis4[j:j+7],2))
print(lis3)

lis2=""
for i in msg2:
    lis2+=format(ord(i),'07b')

