# binarySearch 재귀
Data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def binarySearch(start,end,key):
    global Data
    middle=(start+end)//2
    if Data[middle]<key:
        return binarySearch(middle+1,end,key)
    elif Data[middle]==key:
        return middle
    else:
        return binarySearch(start,middle-1,key)

print(binarySearch(0,len(Data)-1,7))
print(binarySearch(0,len(Data)-1,2))
print(binarySearch(0,len(Data)-1,3))