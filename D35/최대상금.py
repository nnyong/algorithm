import sys,copy
sys.stdin=open('최대상금','r')

T=int(input())
for tc in range(1,T+1):
    data,cnt=map(int,input().split())
    pan=str(data)
    # print(pan)

    def change(pan,count=cnt):
        global max_value
        # if pan in value_list:
        #     if count % 2 == 0:
        #         return
        if count==0:
            # if pan in value_list:
            #     return
            value_list.append(pan)
            value = 0
            for k in range(len(pan)):
                value += int(pan[k]) * (10 ** (len(pan) - k - 1))
            # print(value)
            if value>max_value:
                max_value=value
            set(value_list)
            return

        for i in range(len(pan)):
            for j in range(i+1,len(pan)):
                if pan[i]==pan[j]:
                    continue
                pan=pan[:i]+pan[j]+pan[i+1:j]+pan[i]+pan[j+1:]
                change(pan,count-1)
                pan = pan[:i] + pan[j] + pan[i + 1:j] + pan[i] + pan[j + 1:]
        return
    value_list=[]
    max_value=0
    change(pan)
    print('#{} {}'.format(tc,max_value))



    # max = sorted(pan, reverse=True)
    # print(max)
    # print(pan)
    #
    # while cnt!=0:
    #     result = False
    #     for i in range(len(pan)):
    #         if pan[i]!=max[i]:
    #             for j in range(len(max)):
    #                 if pan[i]==max[j]:
    #                     pan[j],pan[i]=pan[i],pan[j]
    #                     cnt-=1
    #                     result=True
    #                     break
    #         if result:
    #             break
    # if max==pan:
    #     print(max)
    # else:
    #     for i in range(len(max)):
    #























    # # rank=[len(pan)]*len(pan)
    # # print(rank)
    # # for p in range(len(pan)):
    # #     for p2 in range(len(pan)):
    # #         if pan[p]>pan[p2]:
    # #             rank[p]-=1
    # # print(rank)
    # # dict={}
    # # for r in rank:
    # #     if r in dict:
    # #         dict[r]+=1
    # #     else:
    # #         dict[r]=1
    # # print(dict)
    # # for d in dict:
    #
    # def change(pan,count=0):
    #     global max_value
    #     # if pan in value_list:
    #     #     return
    #     # value_list.append(pan[:])
    #     if count==cnt:
    #         value = 0
    #         for k in range(len(pan)):
    #             value += pan[k] * (10 ** (len(pan) - k - 1))
    #         # print(value)
    #         if value>max_value:
    #             max_value=value
    #         return
    #
    #     for i in range(len(pan)):
    #         for j in range(i+1,len(pan)):
    #             if pan[i]==pan[j]:
    #                 continue
    #             pan
    #             # pan[i],pan[j]=pan[j],pan[i]
    #             change(pan,count+1)
    #             # pan[i], pan[j] = pan[j], pan[i]
    #     return
    # value_list=[]
    # max_value=0
    # change(pan)
    # print('#{} {}'.format(tc,max_value))