import sys,time
sys.stdin=open('연습3.txt','r')

data=list(input())
# print(data)

dict={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
data2=''

for i in range(len(data)):
    for j in range(4):
        if data[i].isnumeric():
            if int(data[i])&(1<<3-j):
                data2+='1'
            else:
                data2 += '0'
        else:
            if dict[data[i]]&(1<<3-j):
                data2 += '1'
            else:
                data2 += '0'
print(data2)

password={'001101':0,'010011':1,'111011':2,'110001':3,'100011':4,'110111':5,'001011':6,'111101':7,'011001':8,'101111':9}
pw=[]
for i in range(len(data2)-6):
    pw.append(data2[i:i+6])
print(pw)

i=0
while i<len(pw):
    for p in password.keys():
        if pw[i]==p:
            # stop=i
            print(password[p])
            i += 5
            break
    i+=1