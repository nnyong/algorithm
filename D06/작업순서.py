import sys
sys.stdin=open('작업순서.txt','r')

for tc in range(1,11):
    print(f'#{tc}')
    v, e = map(int, input().split())
    print(v)
    print(e)
    data=list(map(int,input().split()))
    print(data)
    m = [[0] * (v + 1) for i in range(v + 1)]
    print(m)