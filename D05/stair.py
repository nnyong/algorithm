import sys
sys.stdin=open('stair.txt','r')
ans=0
howmany=int(input())

def GetSome(here):
    global ans
    if here==howmany:
        ans+=1
        return
    if here > howmany:
        return
    GetSome(here+1)
    GetSome(here+2)

GetSome(0)

print(f'ans={ans}')