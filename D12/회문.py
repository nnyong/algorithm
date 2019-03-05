import sys
sys.stdin=open('회문.txt','r')

T=int(input())
for tc in range(1,T+1):
    n,m=map(int,input().split())
    l=[]
    for i in range(n):
        l.append(list(input()))
    # print(l)

    center=m//2
    result=[]

    for y in range(n):
        r_center=m//2
        while r_center<=center+(n-m):
            if m % 2:
                a = r_center - 1
                b = r_center + 1
            else:
                a = r_center - 1
                b = r_center
            cnt=0
            for r in range(m//2):
                if l[y][a]==l[y][b]:
                    a-=1
                    b+=1
                    cnt+=1
                else:
                    break
            r_center += 1
        if cnt==center:
            for i in range(m):
                result.append(l[y][a+1])
                a+=1
            break

    for x in range(n):
        c_center=m//2
        while c_center<=center+(n-m):
            if m % 2:
                a = c_center - 1
                b = c_center + 1
            else:
                a = c_center - 1
                b = c_center
            cnt = 0
            for c in range(m//2):
                if l[a][x]==l[b][x]:
                    a-=1
                    b+=1
                    cnt+=1
                else:
                    break
            c_center += 1
        if cnt==center:
            for i in range(m):
                result.append(l[a+1][x])
                a+=1
            break

    print("#{} {}".format(tc,''.join(result)))
