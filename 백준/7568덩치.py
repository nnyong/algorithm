import sys
sys.stdin=open('덩치','r')

n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]

rank=[1]*n
index = 0
while index<n:
    for d in range(len(data)):
        if data[index][0]<data[d][0] and data[index][1]<data[d][1]:
            rank[index]+=1
    index+=1
print(*rank)