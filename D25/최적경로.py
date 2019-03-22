import sys
sys.stdin=open('최적경로.txt','r')

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    data = list(map(int, input().split()))

    start = [(data[0], data[1])]
    end = [(data[2], data[3])]

    custom = []
    for i in range(4, len(data) - 1, 2):
        custom.append((data[i], data[i + 1]))
    # print(custom)

    visited = [0] * n
    result = [0] * n


    def per(depth):
        global min_sum
        if depth == n:
            route = start + result[:] + end
            sum = 0
            for c in range(1, len(route)):
                sum += abs(route[c][0] - route[c - 1][0]) + abs(route[c][1] - route[c - 1][1])
            if sum < min_sum:
                min_sum = sum
            return
        for i in range(n):
            if not visited[i]:
                visited[i] = 1
                result[depth] = custom[i]
                per(depth + 1)
                visited[i] = 0


    min_sum = 987654321
    per(0)
    print('#{} {}'.format(tc, min_sum))