# 전기버스
import sys

sys.stdin=open('4831.txt','r')

T=int(input())
for tc in range(1,T+1):
    number=list(map(int,input().split()))
    K=number[0]
    N=number[1]
    M=number[2]
    charge=list(map(int,input().split()))

    stop=[0]*(N+1)
    for i in range(len(charge)):
        stop[charge[i]]+=1
    print(stop)

    start = 0
    end = K
    cnt=0
    while end < len(stop)-1:
        zero=0
        for i in range(start+1, end+1):
            if stop[i]==1:
                start=i
            else:
                zero+=1
        if zero==K:
            cnt=0
            break
        cnt+=1
        end=start+K
    print(f'#{tc} {cnt}')