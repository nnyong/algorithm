# 특별한 정렬
import sys

sys.stdin=open('4843.txt','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=list(map(int,input().split()))

    # 9
    # 1 2 3 4 5 6 7 8 9
    # 10
    # 1 2 3 4 5 6 7 8 9 10
    # 최대, 최소 두개씩 넣기 위해서 반복 횟수
    if n%2==0:
        N=n//2
    else:
        N=n//2+1

    new_list = []
    for i in range(N):
        min_value=987654321
        max_value=0
        for i in range(len(data)):
            if data[i] != None:
                if data[i]>max_value:
                    max_value=data[i]
                    max_index=i
        for i in range(len(data)):
            if data[i] != None:
                if data[i]<min_value:
                    min_value=data[i]
                    min_index = i
        if max_value==min_value:
            new_list.append(min_value)
        else:
            new_list.append(max_value)
            new_list.append(min_value)

        data[max_index] = None
        data[min_index] =None

    print(f'#{tc}', end=' ')
    for i in new_list[:10]:
        print(i, end=' ')
    print()