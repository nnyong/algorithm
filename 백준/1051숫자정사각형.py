import sys
sys.stdin=open('숫자정사각형','r')
n,m=map(int,input().split())
data=[list(map(int,input())) for _ in range(n)]
# print(data)
if n<=m:
    squa=n
else:
    squa=m

result=False
while squa>0:
    for y in range(n - squa + 1):
        for x in range(m-squa+1):
            if data[y][x] == data[y + squa - 1][x] == data[y][x + squa - 1] == data[y + squa - 1][x + squa - 1]:
                result=squa
                break
            else:
                x += 1
        y+=1
    if result:
        break
    squa-=1
print(result*result)