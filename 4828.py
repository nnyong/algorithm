# min max
import sys
sys.stdin = open('4828.txt', 'r')

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    a=list(map(int,input().split()))
    print(a)

    max_value=a[0]
    min_value=a[0]
    for i in a:
        if i>max_value:
            max_value=i
        elif i<min_value:
            min_value=i
    diff=max_value-min_value

    print(f'#{tc} {diff}')