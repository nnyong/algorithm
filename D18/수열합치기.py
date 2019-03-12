import sys
sys.stdin=open('수열합치기.txt','r')


class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

def Enqueue(lst, h):
    global head
    # p = None
    for i in lst:
        newNode = Node(i)
        if head[h] == None:
            head[h] = newNode
            p = head[h]
        else:
            p.link = newNode
            p = p.link

def merge(node):
    global head
    p0=head[0]
    p=node
    while p0.link!=None:
        if head[0].data>node.data:
            while p.link!=None:
                p=p.link
            p.link=head[0]
            head[0]=node
            return
        if p0.link.data>node.data:
            while p.link!=None:
                p=p.link
            p.link=p0.link
            p0.link=node
            return
        p0=p0.link
    p0.link=node

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    data=[]
    for i in range(m):
        data.append(list(map(int,input().split())))

    head=[None]*m
    for h in range(len(head)):
        Enqueue(data[h],h)



    for i in range(1,len(head)):
        p=head[i]
        merge(p)

    p=head[0]
    result=[]
    while p:
        result.append(p.data)
        p=p.link

    result.reverse()
    result=result[:10]
    print('#{}'.format(tc),end=' ')
    for i in range(len(result)):
        print('{}'.format(result[i]),end=' ')
    print()

    # result=data[0]
    # for seq in range(1,len(data)):
    #     for i in range(len(result)):
    #         j=len(result)-1
    #         if result[i]>data[seq][0]:
    #             # if i==0:
    #             #     for s in range(n):
    #             #         result.insert(i,data[seq][s])
    #             #         i+=1
    #             #     break
    #             # else:
    #             result.append(result[j])
    #             while i!=j:
    #                 result[j]=result[j-1]
    #                 j-=1
    #             result[j]=data[seq][0]
    #             for s in range(1,n):
    #                 result.insert(j+1,data[seq][s])
    #                 j+=1
    #             break
    #         elif i==len(result)-1 and result[i]<=data[seq][0]:
    #             result.extend(data[seq])
    # result.reverse()
    # result=result[:10]
    # print('#{}'.format(tc),end=' ')
    # for i in range(len(result)):
    #     print('{}'.format(result[i]),end=' ')
    # print()
