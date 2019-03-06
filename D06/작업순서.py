import sys
sys.stdin=open('작업순서.txt','r')

for tc in range(1,3):
    print('#{}'.format(tc))
    v, e = list(map(int, input().split()))
    data=list(map(int,input().split()))
    print(data)
    node = [0] * (v + 1)
    myMap=[[0]*(v+1) for i in range(v+1)]
    for i in range(len(data)//2):
        y=data[i*2]
        x=data[i*2+1]
        node[x]+=1
        myMap[y][x]=1
    # print(myMap)
    visited=[0]*(v+1)
    que=[0]*(v+1)
    top=rear=-1
    print(node)

    result=[]
    while node!=[0]*(v+1):
        for i in range(1, v + 1):
            if node[i] == 0 and not visited[i]:
                rear += 1
                que[rear] = i
                break
        while top!=rear:
            top += 1
            y = que[top]
            result.append(y)
            visited[y]=1
            for x in range(len(myMap)):
                if myMap[y][x]==1 and not visited[x] and node[que[top]]<2:
                    rear+=1
                    que[rear]=x
            node[y]-=1