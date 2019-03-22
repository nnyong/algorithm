import sys
sys.stdin=open('화물.txt','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=[list(map(int,input().split())) for _ in range(n)]

    i=0
    l=[]
    while i<n:
        for d in range(i+1,len(data)):
            if data[i][1]>data[d][1]:
                data[i],data[d]=data[d],data[i]
        i+=1
    # print(data)

    i=0
    j=1
    while j<len(data):
        if data[i][1]>data[j][0]:
            data.pop(j)
        else:
            i+=1
            j+=1
    # print(data)

    print('#{} {}'.format(tc,len(data)))