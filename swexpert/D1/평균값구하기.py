import sys
sys.stdin=open('2071','r')

T=int(input())
for tc in range(1,T+1):
    data=list(map(int,input().split()))
    sum=0
    for d in data:
        sum+=d
    avg=round(sum/len(data))
    print('#{} {}'.format(tc,avg))
