def merge(left,right):
    total=len(left)+len(right)
    new_result=[0]*total
    count=0
    left_len=len(left)
    right_len=len(right)
    l_index=0
    r_index=0
    while l_index<left_len and r_index<right_len:
        if right[r_index]>left[l_index]:
            new_result[count]=left[l_index]
            count+=1
            l_index+=1
        else:
            new_result[count] = right[r_index]
            count += 1
            r_index += 1

    if l_index<left_len:
        while l_index!=left_len:
            new_result[count] = left[l_index]
            l_index += 1
            count+=1
    elif r_index<right_len:
        while r_index!=right_len:
            new_result[count] = right[r_index]
            r_index += 1
            count+=1

    return new_result

def mergeSort(data):
    if len(data)<=1: return data
    left=mergeSort(data[:len(data)//2])
    right=mergeSort(data[len(data)//2:])
    return merge(left,right)

print(mergeSort([38,27,43,3,9,82,10]))