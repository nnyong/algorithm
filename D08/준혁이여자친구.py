# 여자친구 만나러 가는 데 드는 최소 비용을 출력한다. 만약 갈 수 없다면 “-1”을 출력.

import sys

sys.stdin=open('준혁.txt','r')

n,m=map(int,input().split())
myMap=[[0]*8 for i in range(8)]
for i in range(m):
    start,end,cost=map(int,input().split())
    myMap[start][end]=cost
    myMap[end][start] = cost

for j in myMap:
    print(j)

visitedNode=[0]*8
min_cost=987654321
def girlfriend(node,cost):
    global min_cost
    visitedNode[1]=True
    if cost >= min_cost:
        return
    if node==7:
        if cost < min_cost:
            min_cost = cost
        return
    for x in range(1,8):
        if not visitedNode[x]:
            x1=x
            node1=node
            if myMap[node][x]:
                visitedNode[x]=True
                a=visitedNode
                b=myMap[node][x]
                girlfriend(x,cost+myMap[node][x])
                visitedNode[x]=False

girlfriend(1,0)
if min_cost==987654321:
    print(-1)
else:
    print(min_cost)