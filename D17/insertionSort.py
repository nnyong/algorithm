data=[1,9,3,6,7,0,4,9,5,5]

for j in range(1, len(data)):
    while True:
        key=data[j]
        i=j-1
        if i<0 or data[i]<=key:
            break
        data[i+1]=data[i]
        i-=1
        j-=1
        data[i+1]=key

print(data)
