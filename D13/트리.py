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

print(m)

def preorder(node):
    if node:
        print(node, end=' ')
        preorder(m[node][0])
        preorder(m[node][1])

def inorder(node):
    if node:
        inorder(m[node][0])
        print(node, end=' ')
        inorder(m[node][1])

def postorder(node):
    if node:
        postorder(m[node][0])
        postorder(m[node][1])
        print(node, end=' ')

print('preorder')
preorder(1)
print()
print('inorder')
inorder(1)
print()
print('postorder')
postorder(1)
print()
print('13의 모든 부모')
parent=[]
p=13
while p!=1:
    parent.append(m[p][3])
    p=m[p][3]
print(parent)


