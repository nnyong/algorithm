import sys
sys.stdin=open('올림픽','r')

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    a_list=list(map(int,input().split()))
    b_list=list(map(int,input().split()))

    new_list=[0]*n
    for b in range(len(b_list)):
        for a in range(len(a_list)):
            if a_list[a]<=b_list[b]:
                new_list[a]+=1
                break
    max_index=0
    max_value=0
    for n in range(len(new_list)):
        if new_list[n]>max_value:
            max_value=new_list[n]
            max_index=n
    print('#{} {}'.format(tc,max_index+1))

