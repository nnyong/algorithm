import sys,time
sys.stdin=open('공통조상','r')
stime=time.time()

def child(begin):
    global front, rear, cnt
    rear += 1
    queue[rear] = begin
    while front != rear:
        front += 1
        start = queue[front]
        for i in range(0, e * 2, 2):
            if data[i] == start:
                cnt += 1
                rear += 1
                queue[rear] = data[i + 1]
    return

T=int(input())
for tc in range(1,T+1):
    v,e,node1,node2=list(map(int,input().split()))
    data=list(map(int,input().split()))

    parent=[0]*(v+1)
    for i in range(0,e*2,2):
        parent[data[i+1]]=data[i]

    n1 = node1
    n2 = node2
    while n1 != parent[n2]:
        if n2 == 1:
            n1 = parent[n1]
            n2 = node2
        n2 = parent[n2]
    common = n1

    cnt=1

    front=rear=-1
    queue=[0]*10000
    child(common)
    print('#{} {} {}'.format(tc,common,cnt))