import sys
sys.stdin=open('bruteforce.txt','r')

T=int(input())
for tc in range(1,T+1):
    str1=list(input())
    str2=list(input())
    # print(str1)
    # print(str2)

    p=0
    result=0
    while p<len(str2)-len(str1)+1:
        k=0
        for i in range(len(str1)):
            if str1[i]==str2[p+i]:
                k+=1
            else:
                break
        if k==len(str1):
            result=1
            break
        p+=1
    print('#{} {}'.format(tc, result))