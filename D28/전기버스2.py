import sys
sys.stdin=open('전기버스','r')

def bustop(stop,charge,ans=0):
    global min_stop
    if stop+charge>=bus[0]:
        if ans<min_stop:
            min_stop=ans
        return
    if ans>min_stop:
        return
    for s in range(1,charge+1):
        bustop(stop+s,bus[stop+s],ans+1)

T=int(input())
for tc in range(1,T+1):
    bus=list(map(int,input().split()))

    min_stop=987654321
    bustop(1,bus[1])
    print('#{} {}'.format(tc,min_stop))























    # start=1
    # charge=bus[1]
    # # print(charge)
    # cnt=0
    # max=0
    # goal=False
    # while True:
    #     for c in range(charge):
    #         start+=1
    #         if start==len(bus):
    #             goal=True
    #             break
    #         if bus[start]>charge and bus[start]>max:
    #             max=bus[start]
    #             new_index=start
    #     if goal:
    #         break
    #     print(new_index)
    #     print(max)
    #     if max==0:
    #         charge=bus[start]
    #     else:
    #         start=new_index
    #         charge=bus[start]
    #     cnt+=1
    # print(cnt)
    #
    #
