# 노드의 거리
import sys
sys.stdin=open('5102.txt','r')

T=int(input())
for tc in range(1,T+1):
    V,E=map(int,input().split())
    myMap = [[0] * (V+1) for i in range(V+1)]
    for i in range(E):
        s,g=map(int,input().split())
        myMap[s][g]=1
        myMap[g][s]=1
    S,G=map(int,input().split())
    # for i in myMap:
    #     print(i)
    # print(f'S={V}, E={E}')
    # print(f'S={S}, G={G}')
    que=[0]*(V+1)
    Distance = [0] * (V+1)
    visited=[0]*(V+1)
    front=rear=-1

    def bfs(here):
        global front,rear,G
        rear+=1
        que[rear]=here
        visited[here]=True
        while front!=rear:
            front+=1
            new=que[front]
            for x in range(1,V+1):
                if myMap[new][x] and not visited[x]:
                    if x==G:
                        Distance[x] = Distance[new] + 1
                        return Distance[G]
                    else:
                        rear+=1
                        que[rear]=x
                        visited[x]=True
                        Distance[x] = Distance[new] + 1
        return Distance[G]

    print(f'#{tc} {bfs(S)}')
