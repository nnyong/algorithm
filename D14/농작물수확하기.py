import sys
sys.stdin=open('농작물.txt','r')
T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=[list(input()) for i in range(n)]
    # print(data)
    map=[[0]*n for i in range(n)]
    start=end=n//2
    for y in range(n):
        if y<n//2:
            if y!=0:
                now=start
                while now!=end+1:
                    map[y][now]=1
                    now+=1
            else:
                map[y][start]=1
            start-=1
            end+=1
        elif y>n//2:
            now = start
            while now != end + 1:
                map[y][now] = 1
                now += 1
            start += 1
            end -= 1
        else:
            now = start
            while now != end + 1:
                map[y][now] = 1
                now += 1
            start += 1
            end -= 1
    # print(map)
    for y in range(n):
        for x in range(n):
            if map[y][x]==1:
                map[y][x]=data[y][x]
    # print(map)
    profit=0
    for i in map:
        for j in i:
            if j!=0:
                profit+=int(j)

    print('#{} {}'.format(tc,profit))

