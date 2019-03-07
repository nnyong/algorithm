import sys
sys.stdin=open('오셀로.txt','r')

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    data=[list(map(int,input().split())) for i in range(m)]
    o=[[0]*n for i in range(n)]
    for y in range(n//2-1,n//2+1):
        for x in range(n//2-1,n//2+1):
            if x==y:
                o[y][x]='w'
            else:
                o[y][x]='b'

    dx=[0,-1,0,1,-1,1,-1,1]
    dy=[-1,0,1,0,-1,1,1,-1]

    print(data)

    for i in range(len(data)):
        y=data[i][1]-1
        x=data[i][0]-1
        if data[i][2]==1:
            o[y][x]='b'
            for dir in range(8):
                cnt=0
                new_y = y + dy[dir]
                new_x = x + dx[dir]
                while new_y >= 0 and new_y < n and new_x >= 0 and new_x < n:
                    if o[new_y][new_x] == 'w':
                        new_y += dy[dir]
                        new_x += dx[dir]
                        cnt+=1
                    elif o[new_y][new_x] == 'b':
                        for k in range(cnt):
                            new_y -= dy[dir]
                            new_x -= dx[dir]
                            o[new_y][new_x]='b'
                        break
                    else:
                        break
        else:
            o[y][x] = 'w'
            for dir in range(8):
                cnt=0
                new_y = y + dy[dir]
                new_x = x + dx[dir]
                while new_y >= 0 and new_y < n and new_x >= 0 and new_x < n:
                    if o[new_y][new_x] == 'b':
                        new_y += dy[dir]
                        new_x += dx[dir]
                        cnt+=1
                    elif o[new_y][new_x] == 'w':
                        for k in range(cnt):
                            new_y -= dy[dir]
                            new_x -= dx[dir]
                            o[new_y][new_x]='w'
                        break
                    else:
                        break
    b_cnt=0
    w_cnt=0
    for i in o:
        for j in i:
            if j=='w':
                w_cnt+=1
            elif j=='b':
                b_cnt+=1
    print('#{} {} {}'.format(tc,b_cnt,w_cnt))