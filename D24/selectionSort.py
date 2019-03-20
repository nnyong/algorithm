import sys
sys.stdin=open('selection.txt','r')

data=list(map(int,input().split()))
print(data)

index=0
def select(l):
    global index
    min=data[index]
    if index==len(l)-1:
        return
    for i in range(index+1,len(l)):
        if min>l[i]:
            min=l[i]
            min_index=i
    l[min_index]=l[index]
    l[index]=min
    index+=1
    select(l)

select(data)
print(data)
