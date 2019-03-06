import sys
sys.stdin=open('단조.txt','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=list(map(int,input().split()))
    max_value=-1
    for i in range(n-1):
        for j in range(i+1,n):
            string=str(data[i]*data[j])
            print(string)
            cnt=0
            for k in range(len(string)-1):
                if string[k+1]<string[k]:
                    cnt+=1
            if int(string)>=max_value and cnt==0:
                max_value=int(string)

    if len(str(max_value))==1:
        print('#{} {}'.format(tc,-1))
    else:
        print('#{} {}'.format(tc, max_value))