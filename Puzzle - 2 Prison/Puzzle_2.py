import os
import re
import random
import hashlib

lis1 = ['Superman','Thor','Thanos','MartianManhunter','Hulk','Batman','BlackPanther','Flash','Ironman','Antman','Spiderman','BlackWidow','Wonderwoman','Hawkeye','Joker','Aquaman','Wolverine','Magneto','Catwoman','DrStrange','Penguin','LexLuthor','Cheetah','HarleyQuinn','DrOcto','GreenGoblin','WinterSoldier','Cyclops','Shazam','GhostRider']
lis2 = ['Mozart','MichaelJackson','AntonioSalieri','HansZimmer','JohnWilliams','DannyElfman','ARRahman','LudwigGöransson','HildurGudnadottir','AlfredNewman','EnnioMorricone','JamesHorner','GustavoSantaolalla','AlexandreDesplat','HowardShore']
lis3 = ['JantarMantar','CortoDeLuces','BBIBP-Corv','SputnikV', 'Comirnaty','mRNA-1273','CoronaVac','Ad5-nCov','EpiVacCorona','BBV152-Covaxin','Ad26COV2S','CoviVac']
lis4 = ['MonkeyMia','Hartsfield–Jackson','OHare','JohnFKennedy','McCarran','PhoenixSkyHarbor','GeorgeBush','LaGuardia','DanielKInouye','GeneralEdwardLawrenceLogan']

#creating a list of paths where Puzzle 3 is stored later
#path = os.path.abspath(os.getcwd())
path='/var/prison/home/billythekid'
destPath = []
for i in range(0,4):    
    for j in range(0,3):
        for k in range(0,2):
            for l in range(0,1):
                tpath = path+'/'+lis1[i]+'/'+lis2[j]+'/'+lis3[k]+'/'+lis4[l]
                destPath.append(tpath)


allPaths=[]
#creating a multiple folders and subfolders
try:
    os.mkdir(path)
except FileExistsError:
    pass
for i in lis1:
    try:
        os.mkdir(path+'/'+i)
    except FileExistsError:
        pass
    for j in lis2:
        try:
            os.mkdir(path+'/'+i+'/'+j)
        except FileExistsError:
            pass
        for k in lis3:
            try:
                os.mkdir(path+'/'+i+'/'+j+'/'+k)
            except FileExistsError:
                pass
            for l in lis4:
                try:
                    tPath = path+'/'+i+'/'+j+'/'+k+'/'+l
                    os.mkdir(tPath)
                    print(tPath)
                    if tPath not in destPath:                    
                        allPaths.append(tPath)
                except FileExistsError:
                    pass


#filePaths are written to a file for Puzzle 3
file = open('/tmp/Puzzle_2.txt', 'w+')
for paths in destPath:
    file.writelines(paths+"\n")
file.close()

file = open('/tmp/allPaths.txt', 'w+')
for paths in allPaths:
    file.writelines(paths+"\n")
file.close()

index = int(random.uniform(0,24))
msg = "Congrats! You've crossed the second gate. This is the path for next Puzzle. Enjoy the music there.\n"+destPath[index]


#creating random files where path for next puzzle is stored
path='/var/ftp/patgarret' 
filename = hashlib.sha256(path.encode()).hexdigest()
tmp="a"
for i in range(0,len(msg)):
    if i%10 == 0 and i//10 != 0:
        tmp = chr(ord(tmp)+1)
              
    filenames = filename+tmp+str(i)
    filePath = path+"/"+filenames+".txt"
    val = format(ord(msg[i]),'08b')
    root = int("0"+val[0:2],2)
    user = int(val[2:5],2)
    grp = int(val[5:],2)
    fd = os.open( filePath, os.O_CREAT)
    os.system("chmod "+ str(root)+str(user)+str(grp)+" "+filePath) 

