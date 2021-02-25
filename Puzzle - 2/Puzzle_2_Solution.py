import os
import stat
def oct_to_str(octal):
     permission=["---","--x","-w-","-wx","r--","r-x","rw-","rwx"]
     result=""
     for __ in [int(n) for n in str(octal)]:
             result+=permission[__]
     return result
 
filename="/var/prison/home/billythekid/"
z=os.listdir(filename)
z=sorted(z)
ans = ""
#getting file permissions from each file in the folder
for f in z:
     a = os.stat("/var/prison/home/billythekid/"+f).st_mode
     b=oct(a)
     if str(b[:4])=="0o10":
             c=oct_to_str(b[-3:])
             c="-"+c
     else:
             c=oct_to_str(b[-3:])
     #accepting the file permissions starting with '---'
     if c[0:3]=="---":
             ans+=c
     else:
             continue

#converting - to 0 and others to 1
p=""
for d in ans:
     if d =="-":
             p+='0'
     else:
             p+='1'
w=""
for i in range(0,len(p),10):
     w+=chr(int(p[i:i+10],2))

print(w)

