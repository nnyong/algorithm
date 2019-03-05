import sys
sys.stdin=open('GNS.txt','r')

T=int(input())
for testcase in range(T):
    tc,n=list(input().split())
    data=list(input().split())

    string_order={'ZRO':0,'ONE':1,'TWO':2, 'THR':3,'FOR':4,'FIV':5, 'SIX':6,'SVN':7, 'EGT':8, 'NIN':9}
    new=[]
    for i in data:
        new.append(string_order[i])
    new.sort()
    # print(new)
    result=[]
    for i in new:
        for j in string_order:
            if string_order[j]==i:
                result.append(j)
    print('{}'.format(tc))
    for i in result:
        print(i,end=' ')
    print()
