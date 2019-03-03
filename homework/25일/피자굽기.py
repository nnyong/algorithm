# 피자굽기
import sys
sys.stdin=open('피자굽기.txt','r')

T=int(input())
for tc in range(1,T+1):
    size, n=map(int,input().split())
    pizza=list(map(int,input().split()))

    o_front=o_rear=-1
    p_front = p_rear = -1

    oven=[0]*size

    print(pizza)

    print(oven)

    for i,c in enumerate(pizza)
        for j in range(size):
            o_rear += 1
            oven[o_rear]=i

