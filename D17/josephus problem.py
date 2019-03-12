n=41
class Node:
    def __init__(self,data,link=None):
        self.data=data
        self.link=link

def Enqueue(item):
    global head,tail
    newNode=Node(item)
    if head==None: head=newNode
    else:
        p=head
        while p.link!=None:
            if p.link.data>newNode.data:
                newNode.link=p.link
                break
            else:
                p=p.link
        p.link = newNode
        tail=newNode

def delete(node):
    node.link=node.link.link

head=None
tail=None

for i in range(1,n+1):
    Enqueue(i)
    if i==n:
        tail.link=head

cnt=n
p=head
while p:
    p=p.link
    delete(p)
    cnt-=1
    if cnt==2:
        p.link.link=None
        break
    p=p.link


while p:
    print(p.data)
    p=p.link
