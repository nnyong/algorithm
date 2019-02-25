# 배열 최소 합
import sys
sys.stdin=open('4881.txt','r')

T=int(input())
for tc in range(1,T+1):
    size=int(input())
    data=[]
    for i in range(size):
        data.append(list(map(int,input().split())))
    # c=data
    visitedX=[0]*(size+1)
    min_value=987654321

    def getSome(y,value):
        global min_value,size
        if value >= min_value:
            return
        if y>size:
            if value<min_value:
                min_value=value
                # b=min_value
            return
        for x in range(1,size+1):
            if not visitedX[x]:
                visitedX[x]=True
                # a=visitedX
                getSome(y+1,value+data[y-1][x-1])
                visitedX[x] = False
    getSome(1,0)
    print(f'#{tc} {min_value}')

