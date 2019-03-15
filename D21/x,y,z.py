# x+y+z=100인 모든 x,y,z 자연수 출력
# x<=y<=z

# 비재귀
cnt=0
for x in range(1,99):
    for y in range(x,99):
        for z in range(y,99):
            if x+y+z==100:
                cnt+=1
                # print((x,y,z))
print(cnt)

# 재귀
visited=[[[0]*100 for _ in range(99)] for __ in range(100)]
cnt2=0
def xyz(x,y,z):
    global cnt2
    if x+y+z>100: return
    if x>y or y>z:
        return
    # if x>98 or y>98 or z>98:
    #     return
    if x+y+z==100:
        cnt2+=1
        return
    if visited[x+1][y][z]==False: visited[x+1][y][z]=True; xyz(x+1,y,z)
    if visited[x][y+1][z] == False: visited[x][y+1][z] = True; xyz(x, y+1, z)
    if visited[x][y][z+1] == False: visited[x][y][z+1] = True; xyz(x, y, z+1)

xyz(1,1,1)
print(cnt2)