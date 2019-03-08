import sys
sys.stdin=open('문자열.txt','r')

T=int(input())
for tc in range(1,T+1):
    a,b=input().split()
    print(a)
    print(b)
    print('안녕~')