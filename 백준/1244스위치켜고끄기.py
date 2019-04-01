import sys
sys.stdin=open('스위치','r')

s=int(input())
switch=list(map(int,input().split()))
n=int(input())
push=[list(map(int,input().split())) for _ in range(n)]
for i in push:
    if i[0]==1:
        num=i[1]
        for j in range(len(switch)):
            if j%num==num-1:
                if switch[j]==0:
                    switch[j]=1
                else:
                    switch[j]=0
    else:
        num=i[1]-1
        left=num-1
        right=num+1
        while switch[left]==switch[right]:
            if left<0 or right>=s:
                break
            left-=1
            right+=1
        left+=1
        right-=1
        for j in range(left,right+1):
            if switch[j] == 0:
                switch[j] = 1
            else:
                switch[j] = 0

# print(switch)
for i in range(len(switch)):
    if i%20==19:
        print(switch[i])
        print()
    else:
        print(switch[i], end=' ')
