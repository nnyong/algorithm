import sys
sys.stdin=open('최소합.txt','r')

def isSafe(x,y):
    if x>=0 and x<n and y>=0 and y<n:
        return True
    else:
        return False

def minsum(x,y,sum):
    global min_sum
    dx=[1,0]
    dy=[0,1]
    if sum>=min_sum:
        return
    if x==n-1 and y==n-1:
        if sum<=min_sum:
            min_sum=sum
        return
    for dir in range(2):
        if isSafe(x + dx[dir], y + dy[dir]):
            minsum(x+dx[dir],y+dy[dir],sum+data[y+dy[dir]][x+dx[dir]])

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=[]
    for i in range(n):
        data.append(list(map(int,input().split())))
    min_sum=987654321
    minsum(0,0,data[0][0])
    print('#{} {}'.format(tc,min_sum))