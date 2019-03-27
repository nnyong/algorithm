import sys
sys.stdin=open('2070','r')

T=int(input())
for tc in range(1,T+1):
    n1,n2=map(int,input().split())
    if n1>n2:
        result='>'
    elif n1==n2:
        result='='
    else:
        result='<'
    print('#{} {}'.format(tc,result))