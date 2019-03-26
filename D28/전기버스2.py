import sys
sys.stdin=open('전기버스','r')

T=int(input())
for tc in range(1,T+1):
    bus=list(map(int,input().split()))
    print(bus)
    start=1
    charge=bus[1]
    # print(charge)
    cnt=0
    max=0
    goal=False
    while True:
        for c in range(charge):
            start+=1
            if start==len(bus):
                goal=True
                break
            if bus[start]>charge and bus[start]>max:
                max=bus[start]
                new_index=start
        if goal:
            break
        print(new_index)
        print(max)
        if max==0:
            charge=bus[start]
        else:
            start=new_index
            charge=bus[start]
        cnt+=1
    print(cnt)


