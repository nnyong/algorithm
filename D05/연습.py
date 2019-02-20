import sys
sys.stdin=open('input.txt','r')

for tc in range(8):
    stack=[0]*100
    top=-1

    info=[0]*128 #char 1byte ASCII code 7bit
    data=input()
    print(data)

    info[ord(')')]='('
    info[ord('}')]='{'
    info[ord(']')]='['
    info[ord('>')]='<'

    howmany=len(data)
    for i in range(howmany):
        if data[i]=='(' or data[i]=='{' or data[i]=='[' or data[i]=='<':
            top+=1
            stack[top]=data[i]
        elif info[ord(data[i])]==stack[top]:
                stack.pop(top)
                top-=1
    print(top)
    print(stack)
    print(howmany)