import sys
sys.stdin=open('이진수2.txt','r')

T=int(input())
for tc in range(1,T+1):
    n=float(input())
    l=[0]*12
    for i in range(1,13):
        if n>=2**(-i):
            n-=2**(-i)
            l[i-1]=1
        else:
            l[i-1]=0
    if n>0:
        print('#{} {}'.format(tc,'overflow'))
    else:
        for i in range(len(l)-1,-1,-1):
            if l[i]==1:
                l=l[0:i+1]
                break
        print('#{}'.format(tc),end=' ')
        print(*l,sep='')