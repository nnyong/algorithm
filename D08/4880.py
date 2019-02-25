# 토너먼트 카드게임
# 3
# 4
# 1 3 2 1
# 6
# 2 1 1 2 3 3
# 7
# 1 3 3 3 1 1 3

import sys

sys.stdin=open('4880.txt','r')

n=6
data=list(map(int,input().split()))
print(data)

def tournament(a,b):
    global data
    if a==1 or b==len(data)-1:
        if data[a]
        return
    if data[a]

    tournament(a,(a+b)//2)
    tournament((a+b)//2+1,b)
    return