# 2072
import sys
sys.stdin=open('2072','r')

T=int(input())
for tc in range(1,T+1):
    data=list(map(int,input().split()))
    sum=0
    for d in data:
        if d%2:
            sum+=d
    print('#{} {}'.format(tc,sum))