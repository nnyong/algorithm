import sys
sys.stdin=open('병합','r')

T=int(input())
for tc in range(1,T+1):
    n=int(input())
    data=list(map(int,input().split()))

    cnt=0
    def merge(left, right):
        global cnt
        total = len(left) + len(right)
        new_result = [0] * total
        count = 0
        left_len = len(left)
        right_len = len(right)
        l_index = 0
        r_index = 0
        while l_index < left_len and r_index < right_len:
            if right[r_index] >= left[l_index]:
                new_result[count] = left[l_index]
                count += 1
                l_index += 1
            else:
                # if r_index==len(right)-1 and l_index==len(left)-1:
                #     cnt += 1
                new_result[count] = right[r_index]
                count += 1
                r_index += 1
        if l_index < left_len:
            while l_index != left_len:
                new_result[count] = left[l_index]
                l_index += 1
                count+=1
            cnt+=1
        elif r_index < right_len:
            while r_index != right_len:
                new_result[count] = right[r_index]
                r_index += 1
                count += 1

        return new_result

    def mergeSort(data):
        if len(data) <= 1: return data
        left = mergeSort(data[:len(data) // 2])
        right = mergeSort(data[len(data) // 2:])
        return merge(left, right)

    result=mergeSort(data)
    print('#{} {} {}'.format(tc,result[len(result)//2],cnt))