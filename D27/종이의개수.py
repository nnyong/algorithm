import sys
sys.stdin=open('종이.txt','r')

n=int(input())
data=[list(map(int,input().split())) for _ in range(n)]
# print(data)

def IsSame(y,x,size):
    value=data[y][x]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if data[j][i]!=value:
                return False
    return True

n0=0
n1=0
nm1=0
def GetSome(y,x,size):
    global n0,n1,nm1
    if IsSame(y,x,size):
        if data[y][x]==0:
            n0+=1
        elif data[y][x]==1:
            n1+=1
        else:
            nm1+=1
    else:
        next=size//3
        for i in range(3):
            for j in range(3):
                GetSome(y+i*next,x+j*next,next)

GetSome(0,0,n)
print(nm1)
print(n0)
print(n1)