import sys
sys.stdin=open('연습4','r')

data=[list(map(int,input().split())) for _ in range(10)]
# print(data)
myMap=[[987654321]*6 for _ in range(6)]
for m in range(len(myMap)):
    myMap[m][m]=0
for d in range(len(data)):
    myMap[data[d][0]][data[d][1]]=data[d][2]

V=[1,2,3,4,5]
def dijkstra(s,Map,D):
    w=0
    while V!=[]:
        min_value = 987654321
        for v in V:
            if D[v]<min_value:
                min_value=D[v]
                w=v
        V.remove(w)
        U.append(w)
        # print(V)
        for i in range(len(D)):
            if D[i]>D[w]+Map[w][i]:
                D[i]=D[w]+Map[w][i]
                parent[i]=w
    return D[5]
U=[0]
D=myMap[0]
parent=[0]*6
print(dijkstra(0,myMap,D))
p=5
while p!=0:
    print(p)
    p=parent[p]
print(p)