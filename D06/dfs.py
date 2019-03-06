# 연습문제3 비재귀
# 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

import sys
sys.stdin=open('dfs.txt','r')

MyMap=[[0]*8 for i in range(8)]
visited=[0]*8
stack=[0]*8
top=-1

def push(x):
    global top
    top+=1
    stack[top]=x

def pop():
    global top
    if top==-1: return 0
    x=stack[top]
    top-=1
    return x

def findnext(here):
    for next in range(8):
        if MyMap[here][next] and not visited[next]:
            return next

def DFS(here):
    global top
    print(here)
    visited[here]=True
    while here:
        next=findnext(here)
        if next:push(here)
        while next:
            here=next
            print(here)
            visited[here]=True
            next=findnext(here)
            push(here)
    here=pop()

data=list(map(int,input().split()))
howmany=int(len(data)/2)

for i in range(howmany):
    start=data[i*2]
    end=data[i*2+1]
    MyMap[start][end]=1
    MyMap[end][start]=1

DFS(1)