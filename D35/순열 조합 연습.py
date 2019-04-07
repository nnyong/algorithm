import itertools

pool = ['A', 'B', 'C']
print(list(itertools.permutations(pool)))
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2))))
print(list(map(''.join, itertools.combinations(pool, 2))))

# def per(begin,ans=''):
#     for i in range(len(pool)):
#
#
# per(0)
