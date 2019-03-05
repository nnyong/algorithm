import sys
sys.stdin=open('중위순회.txt','r')

for tc in range(1,11):
    n=int(input())
    tree=[0]
    for i in range(n):
        tree.append(list(input().split())[1])

    result=[]
    def inorder(node):
        if node*2<len(tree):
            inorder(node*2)
        result.append(tree[node])
        if node * 2+1< len(tree):
            inorder(node*2+1)
        return result

    print('#{}'.format(tc),end=' ')
    for i in inorder(1):
        print(i,end='')
    print()