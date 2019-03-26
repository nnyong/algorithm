import sys
sys.stdin=open('입국심사','r')

n,m=list(map(int,input().split()))
time=[int(input()) for _ in range(n)]
print(time)