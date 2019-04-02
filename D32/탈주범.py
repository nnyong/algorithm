import sys
sys.stdin=open('탈주범','r')

T=int(input())
for tc in range(1,T+1):
    N,M,R,C,L=list(map(int,input().split()))
    data=[list(map(int,input().split())) for _ in range(N)]
    def isSafe(y,x):
        if y<N and y>=0 and x<M and x>=0:
            return True
        else:
            return False

    def bum(y,x):
        global front,rear,cnt
        depth=1
        rear+=1
        queue[rear]=[y,x,data[y][x]]
        while front!=rear:
            front+=1
            y=queue[front][0]
            x=queue[front][1]
            if visited[y][x]==L:
                return
            pipe=queue[front][2]
            for dir in range(4):
                if isSafe(y+dy[dir],x+dx[dir]) and not visited[y+dy[dir]][x+dx[dir]]:
                    if pipe in [1,2,4,7] and dir==0 and  data[y+dy[dir]][x+dx[dir]] in [1,2,5,6]:
                        visited[y + dy[dir]][x + dx[dir]] = visited[y][x]+1
                        rear+=1
                        queue[rear]=[y+dy[dir],x+dx[dir],data[y+dy[dir]][x+dx[dir]]]
                        cnt+=1
                    elif pipe in [1,3,4,5] and dir == 1 and data[y + dy[dir]][x + dx[dir]] in [1, 3,6,7]:
                        visited[y + dy[dir]][x + dx[dir]] = visited[y][x]+1
                        rear += 1
                        queue[rear] = [y + dy[dir], x + dx[dir], data[y + dy[dir]][x + dx[dir]]]
                        cnt += 1
                    elif pipe in [1,2,5,6] and dir == 2 and data[y + dy[dir]][x + dx[dir]] in [1, 2, 4, 7]:
                        visited[y + dy[dir]][x + dx[dir]] = visited[y][x]+1
                        rear += 1
                        queue[rear] = [y + dy[dir], x + dx[dir], data[y + dy[dir]][x + dx[dir]]]
                        cnt += 1
                    elif pipe in [1,3,6,7] and dir == 3 and data[y + dy[dir]][x + dx[dir]] in [1, 3, 4, 5]:
                        visited[y + dy[dir]][x + dx[dir]] = visited[y][x]+1
                        rear += 1
                        queue[rear] = [y + dy[dir], x + dx[dir], data[y + dy[dir]][x + dx[dir]]]
                        cnt += 1

    visited=[[0]*M for _ in range(N)]
    visited[R][C]=1
    dy=[-1,0,1,0]
    dx=[0,1,0,-1]
    cnt=1
    front=rear=-1
    queue=[0]*10000
    bum(R,C)
    print('#{} {}'.format(tc,cnt))

# 0: 1,2,5,6
# 1: 1,3,6,7
# 2: 1,2,4,7
# 3: 1,3,4,5
# 1->0~3
# 2->0,2
# 3->1,3
# 4->0,1
# 5->1,2
# 6->2,3
# 7->0,3
