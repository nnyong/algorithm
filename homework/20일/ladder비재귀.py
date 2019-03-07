# ladder 비재귀
import sys
sys.stdin=open('ladder.txt','r')

for test in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for i in range(100)]
    # print(ladder)
    dx = [-1, 1, 0]
    dy = [0, 0, -1]
    y = 99
    x = 0
    result=0
    while x < 100:
        temp = x
        visited = [[0] * 100 for i in range(100)]
        if ladder[y][x] == 2:
            while y > 0 :
                for dir in range(3):
                    if y + dy[dir] < 0 or x + dx[dir] < 0 or y + dy[dir] > 99 or x + dx[dir] > 99:
                        continue
                    if ladder[y + dy[dir]][x + dx[dir]] == 1 and not visited[y + dy[dir]][x + dx[dir]]:
                        y = y + dy[dir]
                        x = x + dx[dir]
                        visited[y][x] = True
                        break
            result=x
        x = temp + 1
    print('#{} {}'.format(tc,result))
