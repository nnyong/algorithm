Data = [4,6,1,2,8,1,1,0,2,0,3]

print(Data)

count_array=[0]*(max(Data)+1)

for i in Data:
    count_array[i]+=1

# print(count_array)

for i in range(len(count_array)-1):
    count_array[i+1]=count_array[i]+count_array[i+1]

temp=[0]*len(Data)
# print(Data)

for i in range(len(Data)-1, -1, -1):
    count_array[Data[i]] -= 1
    temp[count_array[Data[i]]] = Data[i]

print(temp)


