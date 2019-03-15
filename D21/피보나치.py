# import sys
# sys.stdin=open('input.txt','r')

fibo=[-1]*101
fibo[0]=0
fibo[1]=1

# for now in range(2,101):
#     fibo[now]=fibo[now-1]+fibo[now-2]
#
# print(fibo)

def getSome(num):
    if fibo[num]==-1:
        fibo[num]=getSome(num-1)+getSome(num-2)
        return fibo[num]
    else:
        return fibo[num]

print(getSome(3))