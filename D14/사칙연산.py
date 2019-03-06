import sys
sys.stdin=open('사칙연산.txt','r')

for tc in range(1,11):
    n=int(input())
    # 5
    # 1 - 2 3
    # 2 - 4 5
    # 3 10
    # 4 88
    # 5 65
    data=[]
    for i in range(n):
        data.append(list(input().split()))
    tree=[[0]*3 for i in range(n+1)]
    for i in range(len(data)):
        if len(data[i])==4:
            tree[int(data[i][0])][0]=data[i][1] #value
            tree[int(data[i][0])][1]=int(data[i][2]) #left node
            tree[int(data[i][0])][2] = int(data[i][3]) #right node
        else:
            tree[int(data[i][0])][0]=data[i][1]
    # print(tree)

    l=[]
    def postorder(node):
        if node:
            postorder(tree[node][1])
            postorder(tree[node][2])
            l.append(tree[node][0])
        return l
    post=postorder(1)
    # print(post)

    temp=[]
    for i in post:
        if i.isnumeric():
            temp.append(float(i))
        else:
            if len(temp)>=2:
                n2=temp.pop()
                n1=temp.pop()
                if i=='+':
                    temp.append(n1+n2)
                elif i == '-':
                    temp.append(n1 - n2)
                elif i == '*':
                    temp.append(n1 * n2)
                else:
                    temp.append(n1/n2)
    print('#{} {}'.format(tc,int(temp[0])))