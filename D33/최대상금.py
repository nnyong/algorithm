import sys
sys.stdin=open('최대상금','r')

T=int(input())
for tc in range(1,T+1):
    pan,change=map(int,input().split())
    print(pan,change)