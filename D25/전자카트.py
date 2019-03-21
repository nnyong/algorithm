import sys
sys.stdin=open('전자카트.txt','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=[list(map(int,input().split())) for _ in range(n)]

    def elec(y,sum=0,depth=1):
        global min_sum
        if sum>min_sum:
            return
        if depth==n:
            sum+=data[y][0]
            if sum<=min_sum:
                min_sum=sum
            return
        visited[y]=1
        for i in range(1,n):
            if not visited[i]:
                elec(i,sum+data[y][i],depth+1)
                visited[i]=0

    min_sum=987654321
    visited=[0]*n
    elec(0)
    print('#{} {}'.format(tc,min_sum))