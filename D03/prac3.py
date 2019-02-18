import sys

sys.stdin=open('prac3.txt','r')

def IsSafe(x,y):
    if x>=0 and x<5 and y>=0 and y<5: return True
    else:
        return False

Data = [[0 for x in range(5)] for y in range(5)]

for i in range(5):
    Data[i] = list(map(int,input().split()))

print(Data)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

result=[[0 for x in range(5)] for y in range(5)]

now_x=0
now_y=0
dir=0

for i in range(25):
    min_value = 987654321
    min_x=0
    min_y=0
    for x in range(5):
        for y in range(5):
            if Data[x][y]<min_value:
                min_value=Data[x][y]
                min_x=x
                min_y=y
    result[now_x][now_y]=Data[min_x][min_y]
    Data[min_x][min_y]=987654321

    if IsSafe(now_x+dx[dir],now_y+dy[dir]) and result[now_x+dx[dir]][now_y+dy[dir]]==0:
        now_x=now_x+dx[dir]
        now_y=now_y+dy[dir]
    else:
        dir= (dir+1) % 4
        now_x=now_x+dx[dir]
        now_y=now_y+dy[dir]

print(result)





# for dir in range(4):
#     newY = y + dy[dir]
#     newX = x + dx[dir]
