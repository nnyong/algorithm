import sys
sys.stdin=open('작업순서.txt','r')

for tc in range(1,5):
    print('#{}'.format(tc))
    v, e = list(map(int, input().split()))
    data=list(map(int,input().split()))
    print(data)
    myMap=[[0]*(v+1) for i in range(v+1)]
    node = [0] * (v + 1)
    for i in range(len(data)//2):
        y=data[i*2]
        x=data[i*2+1]
        node[x]+=1
        myMap[y][x]=1
    # print(myMap)
    print(node)

    for i in range(1,v+1):
        if node[i]==0:
            begin=i
            break
    #
    # for y in range(len(myMap)):
    #     for x in range(len(myMap)):
