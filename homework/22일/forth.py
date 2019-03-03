import sys

sys.stdin=open('forth.txt','r')

T=int(input())
for tc in range(1,T+1):
    data=list(input().split())
    stk=[]
    for i in range(len(data)):
        if data[i]=='+' or data[i]=='-' or data[i]=='*' or data[i]=='/':
            if len(stk) < 2:
                result = 'error'
                break
            else:
                n1 = stk.pop()
                n2 = stk.pop()
                if data[i] == '+':
                    stk.append(n2 + n1)
                elif data[i] == '*':
                    stk.append(n2 * n1)
                elif data[i] == '/':
                    stk.append(n2 / n1)
                else:
                    stk.append(n2 - n1)
        elif data[i]=='.':
            if len(stk) != 1:
                result = 'error'
                break
            result = stk.pop()
            if round(result) == result:
                result = round(result)
            break
        else:
            stk.append(float(data[i]))

    print(f'#{tc} {result}')

