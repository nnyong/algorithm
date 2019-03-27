import sys
sys.stdin=open('2068','r')

T=int(input())
for tc in range(1,T+1):
    data=list(map(int,input().split()))
    max=0
    for d in data:
        if d>max:
            max=d
    print('#{} {}'.format(tc,max))