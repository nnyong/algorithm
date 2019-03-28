import sys
sys.stdin=open('보급로.txt','r')

dy=[0,1,0,-1]       #우 하 좌 상
dx=[1,0,-1,0]

def isSafe(x, y):
    if x < n and x >= 0 and y < n and y >= 0:
        return True
    else:
        return False

def path(y, x):
    if y==n-1 and x==n-1:
        return
    for direc in range(4):
        if isSafe(x+dx[direc],y+dy[direc]):
        # if isSafe(x + dx[direc], y + dy[direc]) and not visited[y + dy[direc]][x + dx[direc]]:
            if mountain[y][x]+data[y+dy[direc]][x+dx[direc]]<mountain[y+dy[direc]][x+dx[direc]] and mountain[y][x]+data[y+dy[direc]][x+dx[direc]]<mountain[n-1][n-1]:
                mountain[y+dy[direc]][x+dx[direc]]=mountain[y][x]+data[y+dy[direc]][x+dx[direc]]
                # visited[y+dy[direc]][x+dx[direc]] = True
                path(y + dy[direc], x + dx[direc])
                # visited[y+dy[dir]][x+dx[dir]]=0

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=[list(map(int,input())) for _ in range(n)]
    mountain=[[987654321]*n for _ in range(n)]
    # min_value=987654321
    mountain[0][0]=0
    # visited=[[0]*n for _ in range(n)]
    path(0,0)
    print('#{} {}'.format(tc,mountain[n-1][n-1]))