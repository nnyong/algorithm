# 부분집합의 합
import sys

sys.stdin=open('4837.txt','r')

T=int(input())
for tc in range(1,T+1):
    n,k=map(int,input().split())
    data=[1,2,3,4,5,6,7,8,9,10,11,12]
    cnt=0
    for i in range(1 << 12):
        s = []
        for j in range(13):
            if i & (1 << j):
                s.append(data[j])
        # print(s)
        if len(s)==n and sum(s)==k:
            cnt+=1
    print(f'#{tc} {cnt}')