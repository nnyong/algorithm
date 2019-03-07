import sys
sys.stdin=open('파리.txt','r')

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    array=[list(map(int,input().split())) for i in range(n)]
    # print(array)

    max_fly=0
    for y in range(n-m+1):
        for x in range(n-m+1):
            sum=0
            start=y
            end=x
            for i in range(m):
                for j in range(m):
                    sum+=array[start][end]
                    end+=1
                end=x
                start+=1
            if sum>=max_fly:
                max_fly=sum

    print('#{} {}'.format(tc,max_fly))