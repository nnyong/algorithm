import sys
sys.stdin=open('input.txt','r')

stack=[0]*10
top=-1

# for i in range(1,4):
#     stack.append(i)
#
# while stack:
#     print(stack.pop())

for i in range(1,4):
    top+=1
    stack[top]=i

while top!=-1:
    for i in range(3):
        print(stack[top])
        top-=1