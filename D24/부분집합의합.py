data=[-1,3,-9,6,7,-6,1,5,4,-2]

visited=[0]*len(data)
def subset(index):
    if index==len(data):
        sum=0
        for i in range(len(data)):
            if visited[i]:
                sum+=data[i]
        if sum==0:
            for i in range(len(data)):
                if visited[i]:
                    print(data[i],end=' ')
            print()
        return

    if not visited[index]:
        visited[index]=1
        subset(index+1)
        visited[index]=0
        subset(index+1)
subset(0)




























# visited = [0] * 10

# def GetSome(k, sum):
#     if sum==10 :
#         for i in range(10) :
#             if visited[i]: print("%d " %Data[i], end = " ")
#         print()
#         return
#     if k >=10 or sum > 10 : return
#
#     visited[k] = 1
#     GetSome(k+1, Data[k] + sum)
#     visited[k] = 0
#     GetSome(k+1,  sum)
#
# GetSome(0,0)
