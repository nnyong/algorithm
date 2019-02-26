data=[1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]

MyMap=[[0]*8 for i in range(8)]
howmany=int(len(data)/2)

for i in range(howmany):
    start=data[i*2]
    end=data[i*2+1]
    MyMap[start][end]=1
    MyMap[end][start]=1

front=rear=-1
Queue=[0]*100

visited=[0]*8
Distance=[-1]*10
Parent=[-1]*10

def bfs(here):
    global front,rear
    rear+=1
    Queue[rear]=here
    visited[here]=True
    while front!=rear:
        front+=1
        here=Queue[front]
        print(here)
        for next in range(8):
            if MyMap[here][next] and not visited[next]:
                visited[next]=True
                Distance[next]=Distance[here]+1
                Parent[next]=here
                rear+=1
                Queue[rear]=next

print(bfs(1))
