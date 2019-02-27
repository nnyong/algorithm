# 회전
import sys
sys.stdin=open('5097.txt','r')

def en(item):
    global rear
    rear+=1
    que[rear]=item

def de():
    global front
    front+=1
    return que[front]

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    data=list(map(int,input().split()))
    que = [0] * (len(data)+m)
    front=rear=-1
    for i in range(n):
        en(data[i])

    for i in range(m):
        item=de()
        en(item)
    print(f'#{tc} {que[front+1]}')

