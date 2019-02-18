Data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

key = 7

start = 0
end = len(Data)-1

middle = (start+end)//2

while True:
    if Data[middle] < key:
        start += 1
        middle = (start+end)//2
    elif Data[middle] == key:
        print(middle)
        break
    else:
        end = middle-1
        middle = (start+end)//2
