import sys
sys.stdin=open('베이비진','r')

T=int(input())
for tc in range(1,T+1):
    data=list(map(int,input().split()))

    p1=[0]*10
    p2=[0]*10
    front=-1
    result=0
    end=False
    while front<len(data)-1:
        front+=1
        p1[data[front]]+=1
        for i in range(len(p1)):
            if p1[i]==3:
                result=1
                end=True
                break
        if end:
            break
        for i in range(len(p1)-2):
            if p1[i]>=1 and p1[i+1]>=1 and p1[i+2]>=1:
                result = 1
                end = True
                break
        if end:
            break
        front += 1
        p2[data[front]] += 1
        for i in range(len(p2)):
            if p2[i]==3:
                result = 2
                end = True
                break
        if end:
            break
        for i in range(len(p2)-2):
            if p2[i]>=1 and p2[i+1]>=1 and p2[i+2]>=1:
                result = 2
                end = True
                break
        if end:
            break
    print('#{} {}'.format(tc,result))


