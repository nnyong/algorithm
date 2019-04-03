import sys
sys.stdin=open('정사각형방','r')

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def isSafe(y, x):
    if y >= 0 and y < n and x >= 0 and x < n:
        return True
    else:
        return False

def move(y, x, point):
    global max_d, min_index
    for dir in range(4):
        if isSafe(y + dy[dir], x + dx[dir]):
            if data[y + dy[dir]][x + dx[dir]] == data[y][x] + 1:
                visited[y + dy[dir]][x + dx[dir]] = visited[y][x] + 1
                move(y + dy[dir], x + dx[dir], point)
                return
    if visited[y][x] + 1 > max_d:
        max_d = visited[y][x] + 1
        min_index = point
    elif visited[y][x] + 1 == max_d:
        if point < min_index:
            min_index = point
    return

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=[list(map(int,input().split())) for _ in range(n)]

    max_d=0
    min_index=987654321
    visited=[[0]*n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if not visited[y][x]:
                move(y,x,data[y][x])
    print('#{} {} {}'.format(tc,min_index,max_d))