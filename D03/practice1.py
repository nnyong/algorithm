import sys

sys.stdin = open('practice_input.txt', 'r')

def IsSafe(y,x):
    if x>=0 and x<5 and y>=0 and y<5: return True
    else:
        return False

def Mycalc(a, b):
    if a > b: return a-b
    else: return b-a

Data = [[0 for x in range(5)] for y in range(5)]

for i in range(5):
    Data[i] = list(map(int,input().split()))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

sum = 0
for y in range(5):
    for x in range(5):
        for dir in range(4):
            newY = y+dy[dir]
            newX = x+dx[dir]
            if IsSafe(newY, newX):
                sum += Mycalc(Data[y][x], Data[newY][newX])
print(sum)
