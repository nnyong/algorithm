import sys
sys.stdin=open('트리의순회','r')

T=int(input())
for tc in range(1,T+1):
    inorder=list(input().split())
    post=list(input().split())
    print(inorder,post)
    def preorder(root):


    root=post[len(post)-1]
    preorder(root)
    