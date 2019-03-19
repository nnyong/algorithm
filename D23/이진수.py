import sys
sys.stdin=open('이진수.txt','r')

T=int(input())
for tc in range(1,T+1):
    n,n16=list(input().split())

    dict={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    result=''
    for i in n16:
        if i.isnumeric():
            for j in range(4):
                if int(i)&(1<<3-j):
                    result+='1'
                else:
                    result+='0'
        else:
            for j in range(4):
                if dict[i]&(1<<3-j):
                    result+='1'
                else:
                    result+='0'
    print('#{} {}'.format(tc,result))

