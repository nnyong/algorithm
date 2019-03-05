import sys
sys.stdin=open('글자수.txt','r')

T=int(input())
for tc in range(1,T+1):
    str1=list(input())
    str2=list(input())
    num={}
    for i in str1:
        num[i]=0
    # print(num)

    for i in num:
            for j in str2:
                if j==i:
                    num[i]+=1
    # print(num)

    max_value=0
    for i in num.values():
        if i>max_value:
            max_value=i

    print('#{} {}'.format(tc,max_value))

