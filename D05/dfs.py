import sys
sys.stdin=open('dfs.txt','r')

MyMap=[[0]*8 for i in range(8)]
visited=[0]*8

def DFS(here):
    print(here)
    visited[here]=True

    for next in range(8):
        if MyMap[here][next] and not visited[next]:
            DFS(next)

data=list(map(int,input().split()))
howmany=int(len(data)/2)

for i in range(howmany):
    start=data[i*2]
    end=data[i*2+1]
    MyMap[start][end]=1
    MyMap[end][start]=1

DFS(1)
