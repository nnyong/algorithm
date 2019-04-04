import sys,time
sys.stdin=open('공통조상','r')
stime=time.time()
def par(begin):
    global front, rear
    rear += 1
    queue[rear] = begin
    while front != rear:
        front += 1
        start = queue[front]
        for x in range(v + 1):
            if mymap[start][x]:
                rear += 1
                queue[rear] = x
                parent[x]=start

def bfs2(c):
    global front, rear
    cnt = 0
    rear += 1
    queue[rear] = c
    while front != rear:
        front += 1
        start = queue[front]
        for x in range(v + 1):
            if mymap[start][x]:
                rear += 1
                queue[rear] = x
                cnt += 1
    return cnt

T=int(input())
for tc in range(1,T+1):
    v,e,node1,node2=list(map(int,input().split()))
    data=list(map(int,input().split()))

    mymap=[[0]*(v+1) for _ in range(v+1)]
    for i in range(0,e*2,2):
        mymap[data[i]][data[i+1]]=1

    front = rear = -1
    queue = [0] * 10000
    parent=[0]*(v+1)
    par(1)
    s1=node1
    s2=node2
    while s1!=parent[s2]:
        if s2==1:
            s1=parent[s1]
            s2=node2
        s2=parent[s2]
    common=s1

    front = rear = -1
    queue = [0] * 10000
    child=bfs2(common)
    print('#{} {} {}'.format(tc,common,child+1))
    print(time.time()-stime)