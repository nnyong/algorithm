import sys,copy
sys.stdin=open('최대상금','r')

# T=int(input())
# for tc in range(1,T+1):
#     data,cnt=map(int,input().split())
#     pan=str(data)
#     # print(pan)
#
#     def change(pan,count=cnt):
#         global max_value
#         # if pan in value_list:
#         #     if count % 2 == 0:
#         #         return
#         if count==0:
#             # if pan in value_list:
#             #     return
#             value_list.append(pan)
#             value = 0
#             for k in range(len(pan)):
#                 value += int(pan[k]) * (10 ** (len(pan) - k - 1))
#             # print(value)
#             if value>max_value:
#                 max_value=value
#             return
#
#         for i in range(len(pan)):
#             for j in range(i+1,len(pan)):
#                 if pan[i]==pan[j]:
#                     continue
#                 pan=pan[:i]+pan[j]+pan[i+1:j]+pan[i]+pan[j+1:]
#                 change(pan,count-1)
#                 pan = pan[:i] + pan[j] + pan[i + 1:j] + pan[i] + pan[j + 1:]
#         return
#     value_list=[]
#     max_value=0
#     change(pan)
#     print('#{} {}'.format(tc,max_value))

for i in range(int(input())):
    num, chance = input().split()
    num = [num]
    for t in range(int(chance)):
        result = set([])
        for num_ in num:
            for j in range(len(num_) - 1):
                for k in range(j + 1, len(num_)):
                    if num_[j] == num_[k]:
                        temp = num_
                    else:
                        temp = num_[:j] + num_[k] + num_[j + 1:k] + num_[j] + num_[k + 1:]
                    result.add(temp)
        num = list(result)
    print('#{} {}'.format(i + 1, max(list(map(int, num)))))