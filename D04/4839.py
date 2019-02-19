# 이진탐색 대결
import sys

sys.stdin=open('4839.txt','r')

T=int(input())
for tc in range(1,T+1):
    data=list(map(int,input().split()))

    a_page = data[1]
    l = 1
    r = data[0]
    m=int((l + r) / 2)
    a_cnt = 1
    while m!=a_page:
        if m==l or m==r:
            break
        else:
            if m<a_page:
                l=m
                m=int((l + r) / 2)
            else:
                r=m
                m = int((l + r) / 2)
            a_cnt+=1

    b_page = data[2]
    l = 1
    r = data[0]
    m = int((l + r) / 2)
    b_cnt = 1
    while m != b_page:
        if m == l or m == r:
            break
        else:
            if m < b_page:
                l = m
                m = int((l + r) / 2)
            else:
                r = m
                m = int((l + r) / 2)
            b_cnt += 1

    if a_cnt>b_cnt:
        print(f'#{tc} B')
    elif a_cnt==b_cnt:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} A')