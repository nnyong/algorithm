# binarySearch 재귀
Data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def binarySearch(start,end,key):
    global Data
    middle=(start+end)//2
    if Data[middle]<key:
        binarySearch(start+1,end,key)
    elif Data[middle]==key:
        return middle
    else:
        binarySearch(start,middle-1,key)

result=binarySearch(0,len(Data)-1,7)
print(result)

# Data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# key = 7
#
# start = 0
# end = len(Data)-1
#
# middle = (start+end)//2
#
# while True:
#     if Data[middle] < key:
#         start += 1
#         middle = (start+end)//2
#     elif Data[middle] == key:
#         print(middle)
#         break
#     else:
#         end = middle-1
#         middle = (start+end)//2
