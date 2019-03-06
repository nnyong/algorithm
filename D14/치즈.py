import sys
sys.stdin=open('치즈.txt','r')

c,r=map(int,input().split())
cheese=[[0]*r for i in range(c)]
print(cheese)