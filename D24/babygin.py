import sys
sys.stdin=open('babygin.txt','r')

T=int(input())
for tc in range(1,T+1):
    data=list(map(int,input()))
    # print(data)

    l=[]
    cnt=0
    for a in range(len(data)):
        for b in range(len(data)):
            if a!=b:
                for c in range(len(data)):
                    if a!=c and b!=c:
                        for d in range(len(data)):
                            if a!=d and b!=d and c!=d:
                                for e in range(len(data)):
                                    if a!=e and b!=e and c!=e and d!=e:
                                        for f in range(len(data)):
                                            if a != f and b != f and c != f and d != f and e!=f:
                                                if (data[a],data[b],data[c],data[d],data[e],data[f]) not in l:
                                                    l.append((data[a],data[b],data[c],data[d],data[e],data[f]))
                                                    cnt += 1
    # print(l)
    result=False
    for i in l:
        if i[0]+1==i[1]==i[2]-1 and i[3]+1==i[4]==i[5]-1:
            # print(i)
            result = True
            print('babygin!')
            break
        elif i[0]+1==i[1]==i[2]-1 and i[3]==i[4]==i[5]:
            # print(i)
            result = True
            print('babygin!')
            break
        elif i[0]==i[1]==i[2] and i[3]+1==i[4]==i[5]-1:
            # print(i)
            result = True
            print('babygin!')
            break
        elif i[0]==i[1]==i[2] and i[3]==i[4]==i[5]:
            # print(i)
            result = True
            print('babygin!')
            break
    if result==False:
        print('not babygin!')


