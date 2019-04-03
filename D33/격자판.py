import sys
sys.stdin=open('격자판','r')

T=int(input())
for tc in range(1,T+1):
    data=[list(map(int,input().split())) for _ in range(4)]

    def isSafe(y,x):
        if 0<=y<4 and 0<=x<4:
            return True
        else:
            return False

    def pan(y,x,ans,depth=1):
        global result,cnt
        if depth==7:
            if ans not in result:
                result+=[ans]
                cnt+=1
            return
        for dir in range(4):
            if isSafe(y+dy[dir],x+dx[dir]):
                pan(y+dy[dir],x+dx[dir],ans*10+data[y+dy[dir]][x+dx[dir]],depth+1)


    dy=[0,1,0,-1]
    dx=[1,0,-1,0]
    result=[]
    mymap=[[0]*4 for _ in range(4)]
    cnt=0
    for y in range(4):
        for x in range(4):
            pan(y,x,data[y][x])
    print('#{} {}'.format(tc,cnt))