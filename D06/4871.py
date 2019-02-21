# 그래프경로
import sys
sys.stdin=open('4871.txt', 'r')

T=int(input())
for tc in range(1,T+1):
    v, e=map(int,input().split())
    matrix = [[0] * (v + 1) for i in range(v + 1)]
    for i in range(e):
        # l.append(list(map(int,input().split())))
        a,b=map(int,input().split())
        matrix[a][b]=1
    # print(f'#{tc}')
    # print(matrix)
    S,G=map(int,input().split())

    def find(start,end):
        result=0
        for x in range(len(matrix)):
            temp=matrix[start]
            if matrix[start][x]==1:
                if x==end:
                    return 1
                if find(x,end)==1:
                    return 1

    result=find(S,G)
    if result==1:
        print(f'#{tc} {result}')
    else:
        print(f'#{tc} 0')