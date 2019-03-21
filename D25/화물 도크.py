import sys
sys.stdin=open('화물.txt','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=[list(map(int,input().split())) for _ in range(n)]
    print(data)

    for i in data:
