# 123의 7진수 표현 =>234 나와야 함
num=123
l=[]
while num>=7:
    mod = num % 7
    num=num//7
    l.append(mod)
l.append(num)
l.reverse()
print(*l,sep='')

# 파이썬 못쓰는 경우
data=123

def GetSome(n,k):
    if n<k:
        print(n,end='')
        return
    else:
        GetSome(n//k,k)
        print(n%k,end='')

GetSome(123,7)