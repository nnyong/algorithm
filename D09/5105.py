# 미로의 거리
import sys
sys.stdin=open('5105.txt','r')

dx=[0,-1,0,1]
dy=[-1,0,1,0]

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    maze = [[int(x) for x in input()] for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if maze[y][x]==3:
                goal=(y,x)
            elif maze[y][x]==2:
                start=(y,x)

    que=[0]*(n**2)
    front=rear=-1
    visited=[[0]*n for i in range(n)]
    distance = [[0] * n for i in range(n)]

    def Maze(y,x):
        global front,rear,goal
        rear+=1
        que[rear]=(y,x)
        visited[y][x] = True
        while front!=rear:
            front+=1
            cor=que[front]
            y=cor[0]
            x=cor[1]
            for dir in range(4):
                newY = y + dy[dir]
                newX = x + dx[dir]

                if newY<0 or newY>n-1 or newX<0 or newX>n-1:
                    continue
                if not visited[newY][newX]:
                    if maze[newY][newX] == 0:
                        rear+=1
                        que[rear]=(newY,newX)
                        visited[newY][newX]=True
                        distance[newY][newX]=distance[y][x]+1
                    elif maze[newY][newX]==3:
                        return distance[y][x]
        return 0

    print(f'#{tc} {Maze(start[0],start[1])}')
