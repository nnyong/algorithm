# 숫자->문자열 변환
def itoa(n):
    s=''
    while True:
        s=chr(n%10+48)+s
        n=n//10
        if n==0:
            return s

print(itoa(123))

