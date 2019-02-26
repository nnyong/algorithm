# 회전
import sys
sys.stdin=open('5097.txt','r')

def enQueue(item):
    global rear
    rear+=1
    queue[rear]=item

def deQueue():
    global front
    front+=1
    return queue[front]

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    data=list(map(int,input().split()))
    queue = [0] * (len(data)+m)
    front=rear=-1
    for i in range(n):
        enQueue(data[i])

    for i in range(m):
        item=deQueue()
        enQueue(item)
    print(f'#{tc} {queue[front+1]}')

