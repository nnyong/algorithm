import sys
sys.stdin=open('민석.txt','r')

T=int(input())
for tc in range(1,T+1):
    n,k=map(int,input().split())
    data=list(map(int,input().split()))
    nonSubmit=[]
    for i in range(1,n+1):
        if i not in data:
            nonSubmit.append(i)
    print('#{}'.format(tc),end=' ')
    for i in nonSubmit:
        print(i,end=' ')
    print()
