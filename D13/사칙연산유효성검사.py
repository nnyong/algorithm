import sys
sys.stdin=open('사칙연산.txt','r')

for tc in range(1,11):
    n=int(input())
    data=[]
    for i in range(n):
        data.append(list(input().split()))
    # print(data)

    for i in range(len(data)):
        if len(data[0])!=2:
            data.pop(0)
    # print(data)

    result=1
    for i in data:
        if i[1] in ['*','/','+','-']:
            result=0
            break

    print('#{} {}'.format(tc,result))