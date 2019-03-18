import sys,time
sys.stdin=open('연습2.txt','r')

data=list(input())
# print(data)

dict={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
data2=[]

for i in range(len(data)):
    for j in range(4):
        if data[i].isnumeric():
            if int(data[i])&(1<<3-j):
                data2.append(1)
            else:
                data2.append(0)
        else:
            if dict[data[i]]&(1<<3-j):
                data2.append(1)
            else:
                data2.append(0)
# print(data2)
data2_7=[]
for j in range(0,len(data2),7):
    new=[]
    for i in range(j,j+7):
        if i>=len(data2):
            break
        new.append(data2[i])
    data2_7.append(new)
# print(data2_7)

for i in range(len(data2_7)):
    ans=0
    for j in range(len(data2_7[i])):
        ans+=data2_7[i][len(data2_7[i])-1-j]*2**j
    print(ans)

print(time.time())