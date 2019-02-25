import sys

sys.stdin=open('forth.txt','r')

T=int(input())
for tc in range(1,T+1):
    data=list(input().split())
# data=['2','7','3','+','.']
# # data=['.']
# tc=1
    stack=[]
    # for i in range(len(data)):
    #     if data[i].isnumeric():
    #         stack.append(data[i])
    #     elif data[i]=='.':
    #         if len(stack)==1:
    #             result=stack.pop()
    #             print(f'#{tc} {result}')
    #         else:
    #             print(f'#{tc} error')
    #     else:
    #         if len(stack)>=2:
    #             a=stack.pop()
    #             b=stack.pop()
    #             if data[i]=='*':
    #                 stack.append(int(a)*int(b))
    #             elif data[i]=='+':
    #                 stack.append(int(a)+int(b))
    #             elif data[i]=='-':
    #                 stack.append(int(a)-int(b))
    #             elif data[i]=='/':
    #                 stack.append(int(a)/int(b))
    #         else:
    #             print(f'#{tc} error')
    #             break
    for i in range(len(data)):



