import sys
sys.stdin=open('탈주범','r')

T=int(input())
for tc in range(1,T+1):
    N,M,R,C,L=list(map(int,input().split()))
    print(N,M,R,C,L)
    data=[list(map(int,input().split())) for _ in range(N)]
    print(data)