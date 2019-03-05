import sys
sys.stdin=open('이진힙.txt','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=list(map(int,input().split()))
    tree=[0]
    for i in range(len(data)+1):
        index=len(tree)-1
        if len(tree)>2:
            while index!=1:
                if tree[index]<tree[(index)//2]:
                    tree[index],tree[(index)//2]=tree[(index)//2],tree[index]
                index=(index)//2
        if i==len(data):
            break
        tree.append(data[i])
    # print(tree)

    result=0
    last_index=len(tree)-1
    last_value=tree[last_index]
    while last_index!=1:
        last_index=last_index//2
        result+=tree[last_index]
    print('#{} {}'.format(tc,result))


