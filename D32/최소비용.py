import sys
sys.stdin=open('최소비용','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=[list(map(int,input().split())) for _ in range(n)]
    mymap=[[987654321]*n for _ in range(n)]

    dy=[1,0,-1,0]
    dx=[0,1,0,-1]
    # 하우상좌
    def isSafe(y,x):
        if y<n and y>=0 and x<n and x>=0:
            return True
        else:
            return False

    def cost(y,x):
        global front,rear
        rear+=1
        queue[rear]=[y,x]
        while front != rear:
            front+=1
            new_y=queue[front][0]
            new_x=queue[front][1]
            for dir in range(4):
                if isSafe(new_y+dy[dir],new_x+dx[dir]):
                    if data[new_y+dy[dir]][new_x+dx[dir]]>data[new_y][new_x]:
                        diff=data[new_y + dy[dir]][new_x + dx[dir]]-data[new_y][new_x]
                    else:
                        diff=0
                    if mymap[new_y][new_x]+1+diff<mymap[new_y + dy[dir]][new_x + dx[dir]]:
                        mymap[new_y + dy[dir]][new_x + dx[dir]]=mymap[new_y][new_x] + 1 + diff
                        rear+=1
                        queue[rear]=[new_y+dy[dir],new_x+dx[dir]]

    front=rear=-1
    queue=[0]*100000
    mymap[0][0]=0
    cost(0,0)
    print('#{} {}'.format(tc,mymap[n-1][n-1]))