Data = [2,3,4,7,7,7]

print(Data)

count_array=[0]*(max(Data)+1)

for i in Data:
    count_array[i]+=1

print(count_array)

for i in range(len(count_array)-1):
    count_array[i+1]=count_array[i]+count_array[i+1]

print(count_array)

for i in count_array:
    if i==3:

