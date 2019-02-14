import sys

sys.stdin=open('babygin_input.txt','r')

Data=list(map(int, input().split()))
all=len(Data)
for now in range(all-1):
    for next in range(now+1,all):
        if Data[next]<Data[now]:
            Data[now],Data[next]=Data[next],Data[now]

print(Data)