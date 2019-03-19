import sys
sys.stdin=open('정식이.txt','r')

T=int(input())
for tc in range(1,T+1):
    sum2=list(map(int,input()))
    sum3=list(map(int,input()))
    # print(sum2,sum3)

    list2=[]
    for i in range(len(sum2)):
        temp=sum2[:]
        if temp[i]==1:
            temp[i]=0
            list2.append(temp)
        else:
            temp[i]=1
            list2.append(temp)

    for i in range(len(list2)):
        ans = 0
        for j in range(len(sum2)):
            ans += list2[i][j] * 2 ** (len(sum2)-1 - j)
        list2[i]=ans
    print(list2)

    list3 = []
    for i in range(len(sum3)):
        temp=sum3[:]
        if temp[i]==2:
            temp[i] = 0
            list3.append(temp)
            temp = sum3[:]
            temp[i] = 1
            list3.append(temp)
        elif temp[i]==1:
            temp[i] = 0
            list3.append(temp)
            temp = sum3[:]
            temp[i] = 2
            list3.append(temp)
        else:
            temp[i] = 1
            list3.append(temp)
            temp = sum3[:]
            temp[i] = 2
            list3.append(temp)

    for i in range(len(list3)):
        ans = 0
        for j in range(len(sum3)):
            ans += list3[i][j] * 3 ** (len(sum3)-1 - j)
        list3[i]=ans
    print(list3)

    for i in list2:
        for j in list3:
            if i==j:
                print('#{} {}'.format(tc,i))
                break