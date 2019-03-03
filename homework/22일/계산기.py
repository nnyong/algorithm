import sys

sys.stdin=open('계산기.txt','r')

for tc in range(1,11):
    # print(f'#{tc}')
    n = int(input())
    # print(n)
    data=list(input())
    # print(data)
    opeStk=[]
    post=[]
    for i in data:
        if i.isnumeric():
            post.append(i)
        else:
            if i=='(':
                opeStk.append(i)
            elif i=='*':
                if len(opeStk)>0:
                    if opeStk[len(opeStk)-1]=='*':
                        value=opeStk.pop()
                        post.append(value)
                opeStk.append(i)
            elif i=='+':
                if len(opeStk)>0:
                    if opeStk[len(opeStk)-1]=='+' or opeStk[len(opeStk)-1]=='*':
                        value=opeStk.pop()
                        post.append(value)
                opeStk.append(i)
            else:
                while opeStk[len(opeStk)-1]!='(':
                    value=opeStk.pop()
                    post.append(value)
                opeStk.pop()

    stk=[]
    for i in post:
        if i.isnumeric():
            stk.append(int(i))
        else:
            n2=stk.pop()
            n1=stk.pop()
            if i=='+':
                stk.append(n1+n2)
            else:
                stk.append(n1*n2)
    result=stk.pop()
    print(f'#{tc} {result}')

