# 답:4
# A,B,C: 1, 2, 3
# H: House
import sys
sys.stdin=open('기지국','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=[list(input()) for _ in range(n+1)]
    dx=[0,1,0,-1]
    dy=[-1,0,1,0]
    def isSafe(y,x):
        if y<n+1 and y>=0 and x<n and x>=0:
            return True
        else:
            return False

    for y in range(n+1):
        for x in range(n):
            if data[y][x]=='A':
                for dir in range(4):
                    if isSafe(y+dy[dir],x+dx[dir]):
                        data[y+dy[dir]][x+dx[dir]]='S'
            if data[y][x]=='B':
                for dir in range(4):
                    new_y = y
                    new_x = x
                    for i in range(2):
                        new_y+=dy[dir]
                        new_x+=dx[dir]
                        if isSafe(new_y,new_x):
                            data[new_y][new_x] = 'S'
            if data[y][x]=='C':
                for dir in range(4):
                    new_y = y
                    new_x = x
                    for i in range(3):
                        new_y+=dy[dir]
                        new_x+=dx[dir]
                        if isSafe(new_y,new_x):
                            data[new_y][new_x] = 'S'

    cnt=0
    for y in range(n+1):
        for x in range(n):
            if data[y][x]=='H':
                cnt+=1
    print('#{} {}'.format(tc,cnt))