import sys
sys.stdin=open('미로dfs.txt','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    miro=[list(map(int,input())) for i in range(n)]
    # print(miro)

    dx=[0,-1,0,1]
    dy=[-1,0,1,0]

    for y in range(n):
        for x in range(n):
            if miro[y][x]==2:
                start_y=y
                start_x=x

    def isSafe(y,x):
        if y>=0 and y<n and x>=0 and x<n:
            return True
        else:
            return False

    def dfs(y, x):
        global result
        miro[y][x]=1
        for dir in range(4):
            if isSafe(y+dy[dir],x+dx[dir]):
                if miro[y+dy[dir]][x+dx[dir]] == 0:
                    return dfs(y+dy[dir], x+dx[dir])
                elif miro[y+dy[dir]][x+dx[dir]]==3:
                    result=1
                    return
    result = 0
    dfs(start_y,start_x)
    print('#{} {}'.format(tc, result))