****************************import sys
sys.stdin=open('컨테이너.txt','r')

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    weight=list(map(int,input().split()))
    ton=list(map(int,input().split()))

    w_visited=[0]*n
    t_visited=[0]*m

    result=0
    for r in range(n):
        max_w=0
        max_list=[]
        for w in range(n):
            if weight[w]>=max_w and not w_visited[w]:
                max_w=weight[w]
                max_i=w
        # print(max_w)
        w_visited[max_i]=1
        for t in range(m):
            if ton[t]>=max_w and not t_visited[t]:
                t_visited[t]=1
                result+=max_w
                break
    print('#{} {}'.format(tc,result))

