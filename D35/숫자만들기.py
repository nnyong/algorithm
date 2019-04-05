import sys
sys.stdin=open('숫자','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    operand=list(map(int,input().split()))
    num=list(map(int,input().split()))
    # print(ope)
    print(num)

    op=[]
    for o in range(len(operand)):
        while operand[o]!=0:
            op.append(o)
            operand[o]-=1
    print(op)

    def makenum(n1,n2_index):
        global min_result,max_result
        if n2_index==n:
            if n1<min_result:
                min_result=n1
            if n1>max_result:
                max_result=n1
            return
        for o in range(len(op)):
            if not visited[o]:
                if op[o] == 0:
                    n1 = n1 + num[n2_index]
                elif op[o] == 1:
                    n1 = n1 - num[n2_index]
                elif op[o] == 2:
                    n1 = n1 * num[n2_index]
                else:
                    n1 = n1 // num[n2_index]
                visited[o]=True
                makenum(n1,n2_index+1)
                visited[o] = False

    min_result=987654321
    max_result=0
    visited=[0]*(n-1)
    makenum(num[0],1)
    print(min_result,max_result)


