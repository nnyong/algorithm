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
    print('#{} {}'.format(tc,cnt))


# import sys
# sys.stdin = open("input.txt", "r")
#
# Data = list(map(int, input().split()))
# visited = [0] * 10
#
# def GetSome(k, sum):
#     if sum==10 :
#         for i in range(10) :
#             if visited[i]: print("%d " %Data[i], end = " ")
#         print()
#         return
#     if k >=10 or sum > 10 : return
#
#     visited[k] = 1
#     GetSome(k+1, Data[k] + sum)
#     visited[k] = 0
#     GetSome(k+1,  sum)
#
# GetSome(0,0)
