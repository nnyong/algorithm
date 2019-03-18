# 7bit 10진수
import sys,time
sys.stdin=open('연습1.txt','r')

data=list(map(int,input()))
data2=[]
for j in range(0,len(data),7):
    new=[]
    for i in range(j,j+7):
        new.append(data[i])
    data2.append(new)
print(data2)

for i in range(len(data2)):
    ans=0
    for j in range(7):
        ans+=data2[i][6-j]*2**j
    print(ans)

print(time.time())