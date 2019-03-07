import sys
sys.stdin=open('단어.txt','r')

T=int(input())
for tc in range(1,T+1):
    n,k=map(int, input().split())
    l1=[]
    for i in range(n):
        l1.append(list(map(int,input().split())))
    l2=[]
    for i in range(len(l1)): #0,1,2,3,4
        l=[]
        for j in range(len(l1)): #0,1,2,3,4
            l.append(l1[j][i])
        l2.append(l)

    cnt=0
    for i in l1:
        length=0
        for j in i:
            if j==0:
                if length==k:
                    cnt+=1
                length=0
            else:
                length+=1
        if length==k:
            cnt+=1
    for i in l2:
        length=0
        for j in i:
            if j==0:
                if length==k:
                    cnt+=1
                length=0
            else:
                length+=1
        if length==k:
            cnt+=1
    print('#{} {}'.format(tc,cnt))