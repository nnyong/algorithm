n=[1,2,3,4,5,6,7,8,9]

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

for i in range(len(n)):
    Enqueue(n[i])
    if i==len(n)-1:
        tail.link=head

p=head
while p:
    print(p.data)
    p=p.link

p=head
while p:
    p=p.link
