import sys
sys.stdin=open('input.txt','r')

# for tc in range(8):
#     data=input()
#     print(data)
#     stack=[0]*len(data)
#     top=-1
#     for i in data:
#         if i == ')':
#             stack.pop()
#         else:
#             stack.append(i)
#     # print(stack)
#     if len(stack)>len(data):
#         print('괄호오류')
#     else:
#         print('ok')

# 윤종원 버전
for tc in range(8):
    Data = input()
    N = len(Data)
    stack=[]

    Info = [0] * 128 #Char: 1byte, ASCII: 7bit
    Info[ord(')')] = '('
    Info[ord(']')] = '['
    Info[ord('}')] = '{'
    Info[ord('>')] = '<'

    asc_lst = [40, 41, 60, 62, 91, 93, 123, 125]
    cnt = 0

    for i in range(N):
        if stack == [] and (Data[i] == ")" or Data[i] == "}" or Data[i] == "]" or Data[i] == ">" or ord(Data[i]) not  in asc_lst):
            cnt = 100
            print('Wrong')
            break

        if Data[i] == "(" or Data[i] == "{" or Data[i] == "[" or Data[i] == "<" :
            stack.append(Data[i])
        elif ord(Data[i]) not  in asc_lst:
            continue
        elif Info[ord(Data[i])] == stack[-1]:
            stack.pop()

    if cnt == 100:
        pass
    elif not stack:
        print('Right')
    else:
        print('Wrong')


