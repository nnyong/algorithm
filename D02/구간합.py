# 구간합
import sys

sys.stdin=open('prefix_sum.txt','r')

T=int(input())
for tc in range(1,T+1):

    N,M=map(int,input().split())
    a=list(map(int,input().split()))

    start=0
    end=M
    sum_list=[0]*(len(a)-M+1)
    while end<len(a)+1:
        sum=0
        for i in range(start,end):
            sum+=a[i]
        sum_list[start]+=sum
        start+=1
        end+=1
    diff=max(sum_list)-min(sum_list)
    print(f'#{tc} {diff}')