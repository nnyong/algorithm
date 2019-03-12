# 스도쿠 검증
import sys
import copy

sys.stdin=open('스도쿠.txt','r')

T=int(input())
for tc in range(1,T+1):
    s=[]
    for i in range(9):
        l=list(map(int,input().split()))
        s.append(l)
    s2=copy.deepcopy(s)
    row_check=[]
    for row in s2:
        row.sort()
        if row==[1,2,3,4,5,6,7,8,9]:
            row_check.append(True)
        else:
            row_check.append(False)
    # print(row_check)
    col_list=[]
    for index in range(len(s)):
        l=[]
        for col in range(len(s)):
            l.append(s[col][index])
        col_list.append(l)
    # print(col_list)
    col_check=[]
    for col in col_list:
        col.sort()
        if col==[1,2,3,4,5,6,7,8,9]:
            col_check.append(True)
        else:
            col_check.append(False)
    # print(col_check)
    square_list=[]
    for i in [0,3,6]:
        for j in [0,3,6]:
            l=[]
            for row in range(i,i+3):
                for col in range(j,j+3):
                    l.append(s[row][col])
            square_list.append(l)
    square_check=[]
    for sq in square_list:
        sq.sort()
        if sq==[1,2,3,4,5,6,7,8,9]:
            square_check.append(True)
        else:
            square_check.append(False)
    ck=1
    for ck1 in row_check:
        for ck2 in col_check:
            for ck3 in square_check:
                if ck1==False or ck2==False or ck3==False:
                    ck=0
    print('#{} {}'.format(tc,ck))