# 색칠하기
import sys

sys.stdin=open('4836.txt','r')

T=int(input())

for tc in range(1,T+1):
    N=int(input())
    data=[]
    for i in range(N):
        data.append(list(map(int,input().split())))

    red=[]
    blue=[]
    purple=[]
    for square in data:
        if square[4]==1:
            red.append(square)
        else:
            blue.append(square)
    # print(red)
    # print(blue)

    cnt=0
    for i in range(len(red)):
        for j in range(len(blue)):
            row_cnt = 0
            col_cnt = 0
            for red_row in range(red[i][0],red[i][2]+1):
                for blue_row in range(blue[j][0],blue[j][2]+1):
                    if red_row==blue_row:
                        row_cnt+=1
            for red_col in range(red[i][1],red[i][3]+1):
                    for blue_col in range(blue[j][1],blue[j][3]+1):
                        if red_col==blue_col:
                            col_cnt+=1
            cnt+=row_cnt * col_cnt

    print(f'#{tc} {cnt}')