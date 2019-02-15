import sys

sys.stdin = open('Gravity_input.txt', 'r')

Data = list(map(int, input().split()))

print(Data)

size = len(Data)
max_d = 0
for i in range(size):
    d = size-i
    if Data[i] == 0:
        continue
    else:
        for j in Data[i:]:
            if j >= Data[i]:
                d -= 1
        if d >= max_d:
            max_d = d

print(max_d)
