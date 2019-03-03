import sys
sys.stdin=open('수도요금.txt','r')

T=int(input())
for tc in range(1,T+1):
        w=list(map(int,input().split()))
        P=w[0]
        Q=w[1]
        R=w[2]
        S=w[3]
        W=w[4]

        a_bill=P*W
        if W<=R:
            b_bill=Q
        else:
            b_bill=Q+(W-R)*S

        if a_bill<=b_bill:
            print(f'#{tc} {a_bill}')
        else:
            print(f'#{tc} {b_bill}')