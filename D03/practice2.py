import sys

sys.stdin = open('prac2_input.txt', 'r')

def zero_subset(Data):
    n = len(Data)
    l = []
    for i in range(1 << n):
        s = []
        for j in range(n+1):
            if i & (1 << j):
                s.append(Data[j])
        if sum(s) == 0:
            l.append(True)

    if len(l) > 0:
        return('존재')
    else:
        return('존재하지 않는다.')


Data = list(map(int, input().split()))

print(zero_subset(Data))




