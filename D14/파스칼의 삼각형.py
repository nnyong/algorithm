import sys
sys.stdin=open('파스칼.txt','r')

T=int(input())
for tc in range(1,11):
    n=int(input())
    pascal=[[0]*n for i in range(n)]
    # print(pascal)
    for y in range(n):
        for x in range(n):
            if y==0:
                pascal[y][0]=1
            elif y==1:
                pascal[y][0]=1
                pascal[y][1]=1
            else:
                if x==0:
                    pascal[y][x]=1
                else:
                    for i in range(n-2):
                        pascal[y][x]=pascal[y-1][x-1]+pascal[y-1][x]
    print('#{}'.format(tc))
    for i in pascal:
        for j in i:
            if j!=0:
                print(j,end=' ')
        print()



