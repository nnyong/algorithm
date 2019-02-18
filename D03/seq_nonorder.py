import sys

sys.stdin = open('Search.txt', 'r')

Data = list(map(int, input().split()))

print(Data)

key = 8

index=0
while Data[index] != key:
    result_index=index
    index += 1

print(result_index+1)