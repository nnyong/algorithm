import sys
sys.stdin=open('문자열.txt','r')

T=int(input())
for tc in range(1,T+1):
    a,b=input().split()
    # print(a)
    # print(b)
    a_x=0
    cnt=0
    while True:
        b_x=0
        length = 0
        if a_x >= len(a) or b_x >= len(b):
            break
        for i in range(len(b)):
            if  a_x>=len(a) or b_x>=len(b):
                break
            if a[a_x]==b[b_x]:
                a_x+=1
                b_x+=1
                length+=1
            else:
                a_x-=length-1
                break
        if length==len(b):
            cnt+=1

    result=len(a)-cnt*len(b)+cnt

    print('#{} {}'.format(tc,result))