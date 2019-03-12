import sys
sys.stdin=open('숫자추가.txt','r')

T=int(input())
for tc in range(1,T+1):
    n,m,l=list(map(int,input().split()))
    seq=list(map(int,input().split()))
    # print(seq)
    app=[]
    for i in range(m):
        app.append(list(map(int,input().split())))

    for s in range(m):
        for i in range(len(seq)):
            j=len(seq)-1
            if i==app[s][0]:
                seq.append(seq[j])
                while i!=j:
                    seq[j]=seq[j-1]
                    j-=1
                seq[j]=app[s][1]

    print('#{} {}'.format(tc,seq[l]))