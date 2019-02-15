# view
for test_case in range(1,11):
        a=int(input())
        n=list(map(int,input().split()))

        cnt=0
        for i in range(2,len(n)):
                if n[i]>n[i-1] and n[i]>n[i-2] and n[i]>n[i+1] and n[i]>n[i+2]:
                        cnt+=n[i]-max(n[i-1],n[i-2],n[i+1],n[i+2])
        
        print(f'#{test_case} {cnt}')