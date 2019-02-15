import sys
sys.stdin = open('Flatten_input.txt', 'r')

for tc in range(1,11):
    n = int(input())
    data = list(map(int, input().split()))

    for i in range(n):
        max_value=max(data)
        min_value=min(data)
        max_index=data.index(max_value)
        min_index=data.index(min_value)
        data[max_index]-=1
        data[min_index]+=1

    print(f'#{tc} {max(data)-min(data)}')

