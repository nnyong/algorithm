import sys
sys.stdin=open('이진탐색','r')

T=int(input())
for tc in range(1,T+1):
    # print('#{}'.format(tc))
    n,m=list(map(int,input().split()))
    a=list(map(int,input().split()))
    b = list(map(int, input().split()))
    # print(a,b)
    a.sort()

    def binary(l,r,m,value):
        global result,flag,answer
        if l==r:
            if value==a[l]:
                answer=True
            return
        if value<a[m]:
            if flag=='left':
                result=False
                return
            r=m-1
            m=(l+r)//2
            flag='left'
            binary(l,r,m,value)
        elif value>a[m]:
            if flag=='right':
                result=False
                return
            l = m + 1
            m = (l + r) // 2
            flag = 'right'
            binary(l, r, m,value)
        else:
            answer=True
            return

    l=0
    r=len(a)-1
    m=(l+r)//2
    cnt=0
    for i in range(len(b)):
        flag = 'nope'
        answer=False
        result = True
        value=b[i]
        binary(l,r,m,value)
        if result and answer:
            cnt+=1
    print('#{} {}'.format(tc,cnt))