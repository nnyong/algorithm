# 나사
import sys

sys.stdin=open('metal.txt','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=list(map(int,input().split()))
    len(data)

    l=[]
    index=0
    for i in range(len(data)//2):
        bolt = []
        bolt.append(data[index])
        bolt.append(data[index+1])
        l.append(bolt)
        index+=2

    for n in range(len(l)):
        for key in range(len(l)):
            cnt = 0
            for i in range(len(l)):
                if key == i:
                    continue
                else:
                    if l[key][1] == l[i][0]:
                        if i < key:
                            temp = l[key]
                            for j in range(key - 1, -1, -1):
                                l[j + 1] = l[j]
                            l[0] = temp
                        else:
                            next = l[i]
                            l[i] = l[key + 1]
                            l[key + 1] = next
                        cnt = 1
            if cnt == 0:
                stop_index = key
                # key+1개
                for k in range(key + 1):
                    l.append(l[0])
                    l.remove(l[0])
                break

    print(f'#{tc}',end=' ')
    for i in l:
        for j in i:
            print(j,end=' ')
    print()

#1 2 3 3 4 4 5
#2 5 1 1 2 2 4 4 3
#3 9 5 5 8 8 1 1 2 2 3 3 7
#4 12 2 2 5 5 6 6 9 9 10 10 11 11 1 1 8 8 4 4 15
#5 1 6 6 11 11 10 10 2 2 15 15 17 17 7 7 14
#6 13 15 15 12 12 11 11 7 7 4 4 18 18 6 6 16 16 1 1 10
#7 7 11 11 15 15 8 8 6 6 3 3 12 12 4 4 14 14 10 10 19 19 1 1 13 13 20
#8 2 1 1 22 22 10 10 17 17 25 25 3 3 4 4 13 13 15 15 12 12 8 8 9 9 11 11 18 18 23
#9 26 15 15 3 3 7 7 16 16 9 9 6 6 21 21 14 14 4 4 10 10 17 17 18 18 20 20 23 23 27 27 11 11 8 8 2
#10 20 10 10 21 21 8 8 29 29 28 28 30 30 12 12 14 14 5 5 6 6 15 15 22 22 9 9 16 16 11 11 25 25 4 4 13 13 2 2 1