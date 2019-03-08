import sys
sys.stdin=open('2048.txt','r')

T=int(input())
for tc in range(1,T+1):
    n,s=input().split()
    print(n)
    print(s)
    data=[list(map(int,input().split())) for i in range(int(n))]
    print(data)

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

