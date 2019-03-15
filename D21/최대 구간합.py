data=[5,1,-4,2,-1,-5,-2,8,-3,6]

rangeSum=[0]*len(data)
rangeSum[0]=data[0]
include=[0]*len(data)
max_index=0
start_index=0
for now in range(1,len(data)):
    rangeSum[now]=max(rangeSum[now-1]+data[now],data[now])
    if rangeSum[max_index]<rangeSum[now]:
        max_index=now
        for j in range(start_index,max_index+1):
            include[j]=1
    if max(rangeSum[now-1]+data[now],data[now])==data[now]:
        start_index=now
        for j in range(now+1):
            include[j]=0


print(max(rangeSum))
for i in range(len(data)-1,-1,-1):
    if include[i]==1:
        print(data[i],end=' ')