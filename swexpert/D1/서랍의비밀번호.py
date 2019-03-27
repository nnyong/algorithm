# 2043
import sys
sys.stdin=open('2043','r')

p,k=map(int,input().split())
cnt=1
while p!=k:
    cnt+=1
    k+=1
print(cnt)
