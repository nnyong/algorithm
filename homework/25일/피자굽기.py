# 피자굽기
import sys
sys.stdin=open('피자굽기.txt','r')

T=int(input())
for tc in range(1,T+1):
    size, n=map(int,input().split())
    pizza=list(map(int,input().split()))

    top=-1
    rear=len(pizza)-1
    oven=[]
    for i in range(size):
        top+=1
        oven.append((i+1,pizza[top]))
    # print(oven)

    while len(oven)!=1:
        # for i in range(len(oven)):
        p=oven.pop(0)
        if p[1]//2==0:
            if top!=rear:
                top+=1
                oven.append((top+1,pizza[top]))
        else:
            oven.append((p[0],p[1]//2))
    last_pizza=oven.pop()
    print('#{} {}'.format(tc,last_pizza[0]))


