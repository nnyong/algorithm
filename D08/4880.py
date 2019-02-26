# 토너먼트 카드게임
# 3
# 4
# 1 3 2 1
# 6
# 2 1 1 2 3 3
# 7
# 1 3 3 3 1 1 3

# import sys
#
# sys.stdin=open('4880.txt','r')
#
# n=6
# data=list(map(int,input().split()))
# print(data)
#
# def win(a,b):
#     if data[a-1]==1 and data
# def tournament(a,b):
#     global data
#     if a==1 or b==len(data)-1:
#         if data[a]
#         return
#     if data[a]
#
#     tournament(a,(a+b)//2)
#     tournament((a+b)//2+1,b)
#     return

# 미진이언니꺼
def win(a,b):
    if data[a-1]==1 and data[b-1]==3:
        return a
    elif data[a-1]==3 and data[b-1]==1:
        return b
    else:
        if data[a-1]>=data[b-1]:
            return a
        else:
            return b

def half(start,end):
    if end==start:
        return start
    c=(start+end)//2
    return win(half(start,c),half(c+1,end))

T=int(input())
for tc in range(T):
    N=int(input())
    data=list(map(int,input().split()))
    print(f"#{tc+1} {half(1,N)}")