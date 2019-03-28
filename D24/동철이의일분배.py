import sys
sys.stdin=open('동철이.txt','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=[list(map(int,input().split())) for _ in range(n)]

    def work(y,x,ans=1):
        global max_value
        ans*=data[y][x]*0.01
        if ans<max_value or ans==0:
            return
        else:
            if y==n-1:
                max_value=ans
                return
        visited[x]=True
        for i in range(n):
            if not visited[i]:
                new_x=i
                work(y+1,new_x,ans)
        visited[x]=0

    max_value = 0
    for i in range(n):
        visited=[0]*n
        work(0,i)

    result=max_value*100
    print('#%i %.6f' % (tc,result))