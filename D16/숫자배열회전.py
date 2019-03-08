import sys
sys.stdin=open('숫자배열회전.txt','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=[list(map(int,input().split())) for i in range(n)]

    rotation1=[[0]*n for i in range(n)]
    rotation2=[[0]*n for i in range(n)]
    rotation3=[[0]*n for i in range(n)]

    for y in range(n):
        for x in range(n):
            rotation1[x][n-1-y]=data[y][x]

    for y in range(n):
        for x in range(n):
            rotation2[x][n - 1 - y] = rotation1[y][x]

    for y in range(n):
        for x in range(n):
            rotation3[x][n - 1 - y] = rotation2[y][x]

    print('#{}'.format(tc))
    for i in range(n):
        print(*rotation1[i], end=' ',sep='')
        print(*rotation2[i], end=' ',sep='')
        print(*rotation3[i], end=' ',sep='')
        print()