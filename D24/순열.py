# 5P3
data=[1,2,3,4,5]

# 순열
# l=[]
# for a in range(len(data)):
#     for b in range(len(data)):
#         if a!=b:
#             for c in range(len(data)):
#                 if a!=c and b!=c:
#                     l.append((data[a],data[b],data[c]))
# print(l)

# backtracking
print('순열')
visited=[0]*len(data)
result=[0]*3
def per(depth):
    if depth==3:
        print(result)
        return
    for i in range(len(data)):
        if not visited[i]:
            visited[i]=1
            result[depth]=data[i]
            per(depth+1)
            visited[i]=0
per(0)
print()
print()
# 중복순열
# l=[]
# for a in range(len(data)):
#     for b in range(len(data)):
#         for c in range(len(data)):
#             l.append((data[a],data[b],data[c]))
# print(l)

# backtracking
print('중복순열')
visited=[0]*len(data)
result=[0]*3
def per(depth):
    global cnt
    if depth==3:
        print(result)
        return
    for i in range(len(data)):
        result[depth]=data[i]
        per(depth+1)
per(0)