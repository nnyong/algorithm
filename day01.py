import sys

sys.stdin = open('input.txt', 'r')

Data = list(map(int, input().split()))

print(Data)

max_value = Data[0]
# 최소값
# min_value=987654321
max_index = -1
for i in range(len(Data)):
    if Data[i] >= max_value:
        max_value = Data[i]
        max_index = i

print(max_value)

