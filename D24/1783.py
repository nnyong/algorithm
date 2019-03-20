# 병든 나이트
import sys
sys.stdin=open('1784.txt','r')

h,w=map(int,input().split())
result=0
def sick(n,m):
    global result
    if n==1:
        result=1
    elif n==2:
        result=min(4,(m+1)//2)
        # if m%2:
        #     result=m//2+1
        # else:
        #     result=m//2
    elif n>=3:
        if m>=7:
            result=5+(m-7)
        else:
            result=min(4,m)
sick(h,w)
print(result)