import sys
sys.stdin=open('압축.txt','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=[list(input().split()) for i in range(n)]
    # print(data)
    str=''
    for i in data:
        str+=i[0]*int(i[1])
    # print(str)

    print('#{}'.format(tc))
    for i in range(len(str)):
        if i%10==9:
            print(str[i], end='')
            print()
        else:
            print(str[i], end='')
    print()