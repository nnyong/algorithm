Data = [1,1,1,2,5,7]

print(Data)

count_array=[0]*(max(Data)+1)

for i in Data:
    count_array[i]+=1

# print(count_array)

for i in range(len(count_array)):
    if count_array[i]==3:
        count_array[i]-=3
    elif count_array[i]==6:
        count_array[i]-=6

for i in range(len(count_array)-2):
    if count_array[i]>=1 and count_array[i+1]>=1 and count_array[i+1]:
        count_array[i]-=1
        count_array[i+1]-=1
        count_array[i+2]-=1

# print(count_array)

sum=0
for i in count_array:
    sum+=i

if sum==0:
    print('babygin!')
else:
    print('not babygin')