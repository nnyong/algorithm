import sys
sys.stdin=open('암호.txt','r')

class Node:
    def __init__(self,data,link=None):
        self.data=data
        self.link=link

def Enqueue(node):
    global head,tail
    newNode=Node(node)
    if head==None: head=newNode
    else:
        p=head
        while p.link!=None:
            p = p.link
        p.link=newNode
        tail=newNode

def Enqueue2(node):
    global head


T=int(input())
for tc in range(1,T+1):
    n,m,k=list(map(int, input().split()))
    data=list(map(int,input().split()))
    print(data)

    head=None
    tail=None
    for i in range(len(data)):
        Enqueue(data[i])
    tail.link=head

    p=head
    for i in range(k):
        for rep in range(m-1):
            p=p.link
        Enqueue2(p)

