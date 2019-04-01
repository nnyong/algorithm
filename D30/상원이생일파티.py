import sys
sys.stdin=open('생일','r')

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    data=[list(map(int,input().split())) for _ in range(m)]

    mymap=[[0]*(n+1) for _ in range(n+1)]
    for i in data:
        mymap[i[0]][i[1]]=1
        mymap[i[1]][i[0]] = 1

    # def friend(s):
    #     visited[s]=1
    #     for i in range(1,n+1):
    #         if mymap[s][i]:
    #             distance[i]=s
    #             # print(distance)
    #             friend(i)


    def bfs(here):
        global front, rear
        rear += 1
        Queue[rear] = here
        while front != rear:
            front += 1
            here = Queue[front]
            # print(here)
            for next in range(n+1):
                if mymap[here][next] and not visited[next]:
                    visited[next]=True
                    distance[next] = distance[here] + 1
                    rear += 1
                    Queue[rear] = next

    visited=[0]*(n+1)
    front = rear = -1
    Queue = [0] * 500
    distance = [0] * (n+1)
    # friend(1)
    bfs(1)
    print(distance)

    cnt=0
    for i in distance:
        if i==1 or i==2:
            cnt+=1
    print('#{} {}'.format(tc,cnt))