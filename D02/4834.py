# 숫자카드
import sys

sys.stdin=open('4834.txt','r')

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    a=list(map(int,input().split()))[0]

    a_l=[]
    for i in str(a):
        a_l.append(int(i))

    count_array=[0]*(max(a_l)+1)

    for i in range(len(a_l)):
        count_array[a_l[i]]+=1

    max_value=count_array[0]
    for i in range(len(count_array)):
        if count_array[i]>=max_value:
            max_value=count_array[i]

            max_index=i

    print(f'#{tc} {max_index} {max_value}')
