import sys
sys.stdin=open('웜','r')

n=int(input())
m=int(input())
data=[list(map(int,input().split())) for _ in range(m)]
print(data)

map=[[0]*(n+1) for _ in range(n+1)]
print(map)

for d in data:
    map[d[0]][d[1]]=1
    map[d[1]][d[0]] = 1
print(map)

