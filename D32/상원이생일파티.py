import sys
sys.stdin=open('생일파티','r')

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    data=[list(map(int,input().split())) for _ in range(m)]

    mymap=[[0]*(n+1) for _ in range(n+1)]

    for d in data:
        mymap[d[0]][d[1]]=1
        mymap[d[1]][d[0]] = 1

    def friend(start):
        global front, rear
        rear+=1
        queue[rear]=start
        while front!=rear:
            front+=1
            new_start=queue[front]
            visited[new_start]=True
            for end in range(n+1):
                if mymap[new_start][end] and not visited[end]:
                    if distance[end]>0:
                        continue
                    if distance[new_start]>=2:
                        return
                    else:
                        distance[end]=distance[new_start]+1
                        rear+=1
                        queue[rear]=end

    front=rear=-1
    queue=[0]*500
    visited=[0]*(n+1)
    distance=[0]*(n+1)
    friend(1)
    # print(distance)

    cnt=0
    for i in distance:
        if i!=0:
            cnt+=1
    print('#{} {}'.format(tc,cnt))