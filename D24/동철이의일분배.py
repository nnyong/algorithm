import sys
sys.stdin=open('동철이.txt','r')

# def work(depth):
#     global result
#     if depth == n:
#         for i in range(n):
#             per[i]=data[i][index[i]]
#         ans=1
#         for i in range(n):
#             ans*=per[i]
#         # ans/=(100**(n-1))
#         if ans>=result:
#             result=ans
#         return
#     for i in range(n):
#         if not visited[i]:
#             visited[i] = 1
#             index[depth] = i
#             work(depth + 1)
#             visited[i] = 0
def work(depth,ans=1):
    global result
    if ans<result:
        return
    if depth == n:
        if ans>=result:
            result=ans
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            index[depth] = i
            # per[i] = data[i][index[i]]/(100 ** (n - 1))
            # ans*=per[i]
            ans*=data[i][index[i]]/(100 ** (n - 1))
            work(depth + 1,ans)
            visited[i] = 0

T=int(input())
for tc in range(1,T+1):
    # print('#{}'.format(tc))
    n=int(input())
    data=[]
    for i in range(n):
        data.append(list(map(int,input().split())))
    # print(data)

    visited = [0] * n
    index = [0] * n
    per = [0] * n
    result=0
    work(0)
    print('#%i %.6f' % (tc,result))

    # 4
    # 71
    # 51
    # 30
    # 1
    # 29
    # 63
    # 32
    # 93
    # 84
    # 94
    # 33
    # 21
    # 56
    # 40
    # 80
    # 31