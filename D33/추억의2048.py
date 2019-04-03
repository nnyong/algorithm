import sys
sys.stdin=open('추억의2048','r')

def push(s):
    if s == 'up':
        for y in range(1, n):
            for x in range(n):
                if data[y][x]:
                    for i in range(y - 1, -1, -1):
                        if data[i][x] == 0:
                            data[i][x] = data[i + 1][x]
                            data[i + 1][x] = 0
    elif s == 'down':
        for y in range(n - 2, -1, -1):
            for x in range(n):
                if data[y][x]:
                    for i in range(y + 1, n):
                        if data[i][x] == 0:
                            data[i][x] = data[i - 1][x]
                            data[i - 1][x] = 0
    elif s == 'left':
        for x in range(1, n):
            for y in range(n):
                if data[y][x]:
                    for i in range(x - 1, -1, -1):
                        if data[y][i] == 0:
                            data[y][i] = data[y][i + 1]
                            data[y][i + 1] = 0
    elif s == 'right':
        for x in range(n - 2, -1, -1):
            for y in range(n):
                if data[y][x]:
                    for i in range(x + 1, n):
                        if data[y][i] == 0:
                            data[y][i] = data[y][i - 1]
                            data[y][i - 1] = 0


def plus(s):
    if s == 'up':
        for x in range(n):
            for y in range(n - 1):
                if data[y][x] == data[y + 1][x]:
                    data[y][x] *= 2
                    data[y + 1][x] = 0
    elif s == 'down':
        for y in range(n - 1, 0, -1):
            for x in range(n):
                if data[y][x] == data[y - 1][x]:
                    data[y][x] *= 2
                    data[y - 1][x] = 0
    elif s == 'left':
        for x in range(n - 1):
            for y in range(n):
                if data[y][x] == data[y][x + 1]:
                    data[y][x] *= 2
                    data[y][x + 1] = 0
    elif s == 'right':
        for x in range(n - 1, 0, -1):
            for y in range(n):
                if data[y][x] == data[y][x - 1]:
                    data[y][x] *= 2
                    data[y][x - 1] = 0

T=int(input())
for tc in range(1,T+1):
    n,s=list(input().split())
    n=int(n)
    data=[list(map(int,input().split())) for _ in range(n)]

    push(s)
    plus(s)
    push(s)
    print('#{}'.format(tc))
    for d in data:
        print(*d)