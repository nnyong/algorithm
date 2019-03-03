import sys
sys.stdin=open('contact.txt','r')

T=10
for tc in range(1,T+1):
    print(f'#{tc}')
    cont=[[0]*101 for i in range(101)]
    n, begin=list(map(int,input().split()))
    print(n)
    print(begin)
    data=list(map(int,input().split()))
    print(data)
    for i in range(n//2):
        start=data[i*2]
        end=data[i*2+1]
        cont[start][end]=1
    for j in cont:
        print(j)

    que=[0]*101
    visited=[0]*101
    top=-1
    rear=-1
    def contact(begin):
        global top,rear,cont
        rear+=1
        que[rear]=begin
        visited[begin]=True
        while True:
            top+=1
            y=que[top]
            for x in range(101):
                if cont[y][x]==1:
                    rear+=1
                    que[rear]=x

    contact(begin)