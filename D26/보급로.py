import sys
sys.stdin=open('보급로.txt','r')

dy=[0,1,0,-1]
dx=[1,0,-1,0]

def isSafe(x, y):
    if x < n and x >= 0 and y < n and y >= 0:
        return True
    else:
        return False

def path(y, x, ans=0):
    global min_value
    visited[y][x]=True
    ans += data[y][x]
    if ans>min_value:
        return
    if y==n-1 and x==n-1:
        min_value=ans
        return
    for dir in range(4):
        if isSafe(x+dx[dir],y+dy[dir]) and not visited[y+dy[dir]][x+dx[dir]]:
            path(y + dy[dir], x + dx[dir],ans)
            visited[y+dy[dir]][x+dx[dir]]=0


T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=[list(map(int,input())) for _ in range(n)]

    visited=[[0]*n for _ in range(n)]
    min_value=987654321
    path(0,0)
    print('#{} {}'.format(tc,min_value))