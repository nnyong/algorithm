# 괄호검사
import sys

sys.stdin=open('4866.txt','r')

T=int(input())
for tc in range(1,T+1):
    data=input()
    N=len(data)
    stack = []
    # print(data)

    Info = [0] * 128  # Char: 1byte, ASCII: 7bit
    Info[ord(')')] = '('
    # Info[ord(']')] = '['
    Info[ord('}')] = '{'
    # Info[ord('>')] = '<'

    top=-1
    for i in range(N):

        if data[i] == '(' or data[i] == '{':
            stack.append(data[i])
            top += 1
        else:
            if top >= 0:
                if stack[top] == Info[ord(data[i])]:
                    stack.pop()
                    top -= 1
                elif (data[i] == '}' or data[i] == ')') and data[i] not in stack:
                    top=0
                    break
            else:
                if data[i] == ')' or data[i] == '}':
                    top = 0
                    break
    print(f'#{tc}', end=' ')
    if top==-1:
        print(1)
    else:
        print(0)


