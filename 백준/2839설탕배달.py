n=15
cnt=0
num3=0
num5=n//5
while num5>-1:
    divide=n-5*num5
    if divide%3==0:
        num3=divide//3
        cnt=num5+num3
        break
    else:
        num5-=1
if cnt==0:
    print(-1)
else:
    print(cnt)
