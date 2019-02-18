# 행,열, 대각선 최대합
import sys

sys.stdin=open('sum.txt', 'r')

for tc in range(1, 11):
    n=int(input())
    data=[]
    for row in range(100):
        data.append(list(map(int,input().split())))
    # print(data)
    # 행 최대값
    row_sum=[]
    for row in data:
        row_sum.append(sum(row))
    # print(row_sum)
    row_max=max(row_sum)
    # print(row_max)
    # 열 최대값
    col_sum=[]
    for col in range(100):
        sum_value=0
        for row in range(100):
            sum_value+=data[row][col]
        col_sum.append(sum_value)
    # print(col_sum)
    col_max=max(col_sum)
    # print(col_max)
    # 대각선 최대값
    cross=[]
    cross_sum1=0
    for row in range(100):
        for col in range(100):
            if row==col:
                cross_sum1+=data[row][col]
    cross.append(cross_sum1)

    cross_sum2=0
    for row in range(100):
        for col in range(99,-1,-1):
            if col==99-row:
                cross_sum2+=data[row][col]
    cross.append(cross_sum2)
    # print(cross)
    cross_max=max(cross)
    # print(cross_max)

    result=max(row_max,col_max,cross_max)

    print(f'#{tc} {result}')