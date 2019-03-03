# 종이붙이기
import sys

sys.stdin=open('4869.txt','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())

    def paper(x):
        while x>=30:
            return paper(x-10)+paper(x-20)*2
        if x==20:
            return 3
        elif x==10:
            return 1

    result=paper(n)

    print(f'#{tc} {result}')
