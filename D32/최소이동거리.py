import sys
sys.stdin=open('최소이동거리','r')

T=int(input())
for tc in range(1,T+1):
    N,E=map(int,input().split())
    data=[list(map(int,input().split())) for _ in range(E)]
    mymap=[[0]*(N+1) for _ in range(N+1)]
    for d in data:
        mymap[d[0]][d[1]]=d[2]

    def move(begin):
        global front,rear
        rear+=1
        queue[rear]=begin
        while front!=rear:
            front += 1
            start=queue[front]
            for end in range(N+1):
                if mymap[start][end]:
                    if d[start]+mymap[start][end]<d[end]:
                        d[end]=d[start]+mymap[start][end]
                        rear+=1
                        queue[rear]=end

    front=rear=-1
    queue=[0]*100000
    d=[987654321]*(N+1)
    d[0]=0
    move(0)
    print('#{} {}'.format(tc,d[N]))