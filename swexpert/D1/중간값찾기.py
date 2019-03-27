import sys
sys.stdin=open('2063','r')

n=int(input())
data=list(map(int,input().split()))
data.sort()
result=data[len(data)//2]
print(result)