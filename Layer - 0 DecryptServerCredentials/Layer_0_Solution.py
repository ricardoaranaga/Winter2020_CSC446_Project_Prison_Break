#read lines from text file
file = open('Puzzle_0.txt','r')
lis = file.readlines()
file.close()

encodedMsg = lis[-1]

#decrypting the encrypted message by dividing the ASCII value by 2
lis2=""
for i in encodedMsg:
    lis2+= str(ord(i)%2)

#append the binary value and getting the characters
lis3 = ""
for j in range(0,len(lis2),7):
    lis3+= chr(int(lis2[j:j+7],2))
print(lis3)

