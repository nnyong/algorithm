import sys
sys.stdin=open('quick','r')

T=int(input())
for tc in range(1,T+1):
    data=list(map(int,input().split()))
    # print(data)

    def partition(data,l,r):
        pivot=data[l]
        i=l
        j=r
        while i<j:
            while data[i]<=pivot and i<r:
                i+=1
            while data[j]>=pivot and j>l:
                j-=1
            if i<j:
                data[i], data[j] = data[j], data[i]
        data[l], data[j] = data[j], data[l]
        return j

    def quickSort(data,l,r):
        if l<r:
            s=partition(data,l,r)
            quickSort(data,l,s-1)
            quickSort(data, s+1, r)

    quickSort(data,0,len(data)-1)
    print(data)