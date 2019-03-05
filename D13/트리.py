import sys
sys.stdin = open('트리.txt','r')

v = int(input())
data = list(map(int, input().split()))
m=[[0]*5 for i in range(v+1)]

visited = [0]*(v+1)
for i in range(len(data)//2):
    if i == 0:
        m[data[0]][4] = 0
    if not visited[data[i*2]]:
        m[data[i*2]][0] = data[i*2+1]
        m[data[i*2+1]][3] = data[i*2]
        m[data[i*2+1]][4] = m[data[i*2]][4]+1
        m[data[i*2]][2] += 1
        visited[data[i*2]] = True
    else:
        m[data[i*2]][1] = data[i*2+1]
        m[data[i * 2 + 1]][3] = data[i * 2]
        m[data[i * 2 + 1]][4] = m[data[i * 2]][4] + 1
        m[data[i*2]][2] += 1

for i in range(len(m)):
    print('{} {}'.format(i, m[i]))
