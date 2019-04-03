import sys

sys.stdin = open('magnetic', 'r')


def push(y, x, mag):
    if mag == 1:
        if y == n - 1:
            data[y][x] = 0
            return
        for i in range(y + 1, n):
            if data[i][x] == 2:
                return
            elif data[i][x] == 1:
                continue
                return
            else:
                if i == n - 1:
                    data[i - 1][x] = 0
                    data[i][x] = 0
                    return
                data[i - 1][x] = 0
                data[i][x] = 1
    else:
        if y == 0:
            data[y][x] = 0
            return
        for i in range(y - 1, -1, -1):
            if data[i][x] == 0:
                if i == 0:
                    data[i + 1][x] = 0
                    data[i][x] = 0
                    return
                data[i][x] = 2
                data[i + 1][x] = 0
            else:
                return
    return


for tc in range(1, 10 + 1):
    n = int(input())
    data = [list(map(int, input().split())) for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if data[y][x] == 1:
                push(y, x, 1)
            if data[y][x] == 2:
                push(y, x, 2)
    cnt = 0
    for y in range(n):
        for x in range(n):
            if data[y][x] == 1:
                if data[y + 1][x] == 2:
                    cnt += 1
    print('#{} {}'.format(tc, cnt))