import sys
sys.stdin=open('숫자','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    operand=list(map(int,input().split()))
    num=list(map(int,input().split()))

    op=[]
    for o in range(len(operand)):
        while operand[o]!=0:
            op.append(o)
            operand[o]-=1

    def makenum(n1,n2_index=1):
        global min_result,max_result
        if n2_index==n:
            if n1<min_result:
                min_result=n1
            if n1>max_result:
                max_result=n1
            return
        for o in range(len(op)):
            if not visited[o]:
                if o >= 1:
                    if op[o] == op[o - 1] and not visited[o-1]:
                        continue
                if op[o] == 0:
                    visited[o] = True
                    makenum(n1+num[n2_index], n2_index + 1)
                    visited[o] = False
                elif op[o] == 1:
                    visited[o] = True
                    makenum(n1 - num[n2_index], n2_index + 1)
                    visited[o] = False
                elif op[o] == 2:
                    visited[o] = True
                    makenum(n1 * num[n2_index], n2_index + 1)
                    visited[o] = False
                else:
                    visited[o] = True
                    makenum(int(n1 / num[n2_index]), n2_index + 1)
                    visited[o] = False


    min_result=987654321
    max_result=-987654321
    visited=[0]*(n-1)
    makenum(num[0])
    result=max_result-min_result
    print('#{} {}'.format(tc,result))


