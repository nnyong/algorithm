import sys
sys.stdin=open('단조.txt','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=list(map(int,input().split()))
    max_value=0
    for i in range(n):
        for j in range(i+1,n):
            string=str(data[i]*data[j])
            # print(string)
            for k in range(len(string)-1):
                if string[k+1]<string[k]:
                    continue
                if int(string)>=max_value:
                    max_value=int(string)

    if len(str(max_value))==1:
        print('#{} {}'.format(tc,-1))
    else:
        print('#{} {}'.format(tc, max_value))
