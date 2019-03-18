import sys
sys.stdin=open('단순.txt','r')

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    # print(n)
    # print(m)
    data=[]
    for i in range(n):
        data.append(input())
    # print(data)

    dict={'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}

    for row in data:
        if '1' in row:
            for i in range(len(row)-1,-1,-1):
                if row[i]=='1':
                    pw=row[i-55:i+1]
                    break
    # print(pw)
    pw_7bit=[]
    for i in range(0,len(pw),7):
        pw_7bit.append(pw[i:i+7])
    # print(pw_7bit)

    pnum=[]
    for b in range(len(pw_7bit)):
        for k in dict.keys():
            if pw_7bit[b]==k:
                pnum.append(dict[k])
                break
    # print(pnum)

    odd=0
    even=0
    for n in range(len(pnum)):
        if n%2:
            odd+=pnum[n]
        else:
            even+=pnum[n]
    result=even*3+odd
    # print(result)

    if result%10==0:
        print('#{} {}'.format(tc,sum(pnum)))
    else:
        print('#{} {}'.format(tc, 0))