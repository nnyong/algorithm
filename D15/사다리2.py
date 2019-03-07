import sys
sys.stdin=open('사다리2.txt','r')

for test in range(1,2):
    tc=int(input())
    ladder=[list(map(int,input().split())) for i in range(100)]
    # print(ladder)
    distance=[0]*100
    dx=[-1,1,0]
    dy=[0,0,1]
    y=x=0
    while x<100:
        temp = x
        visited = [[0] * 100 for i in range(100)]
        if ladder[y][x]==1:
            while y<9:
                for dir in range(3):
                    if y+dy[dir]<0 or x+dx[dir]<0 or y+dy[dir]>99 or x+dx[dir]>99:
                        continue
                    if ladder[y+dy[dir]][x+dx[dir]]==1 and not visited[y+dy[dir]][x+dx[dir]]:
                        y=y+dy[dir]
                        x=x+dx[dir]
                        visited[y][x]=True
                        distance[temp]+=1
                        break
        x=temp+1
        y=0
    print(distance)
    max_distance=0
    for i in range(len(distance)):
        if distance[i]>=max_distance:
            max_distance=distance[i]
            result=i
    print(result)