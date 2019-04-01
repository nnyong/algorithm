import sys
sys.stdin=open('리모콘','r')
n=input()
r=int(input())
if r==0:
    data=[]
else:
    data=list(map(int,input().split()))




























ans=target-100
if ans<0: ans=-ans

for now in range(1000001):
    channel=now
    len=Ispossible(channel)

    if len>0:
        press=channel-target
        if press<0:

        if

# min_result=987654321
#
# def updown(n):
#     if n=='100':
#         return 0
#     if n=='101':
#         return 1
#     if n=='102':
#         return 2
#     new_n=''
#     for i in range(len(n)):
#         if int(n[i]) in data:
#             num=int(n[i])
#             if num==0:
#                 updown(new_n)
#                 return
#             while num in data:
#                 num-=1
#             new_n+=str(num)
#             if i<len(n)-1:
#                 break
#         else:
#             new_n+=n[i]
#     if len(new_n)<len(n):
#         value=9
#         while value in data:
#             value-=1
#         for i in range(len(n)-len(new_n)):
#             new_n+=str(value)
#     # print(new_n)
#     cnt=len(n)
#     cnt += int(n) - int(new_n)
#     return cnt
#
# def downup(n):
#     if n=='100':
#         return 0
#     if n=='99':
#         return 1
#     new_n=''
#     for i in range(len(n)):
#         if int(n[i]) in data:
#             num=int(n[i])
#             while num in data:
#                 num+=1
#             new_n+=str(num)
#             if i<len(n)-1:
#                 break
#         else:
#             new_n+=n[i]
#     if len(new_n)<len(n):
#         value=0
#         while value in data:
#             value+=1
#         for i in range(len(n)-len(new_n)):
#             new_n+=str(value)
#     # print(new_n)
#     cnt=len(n)
#     cnt+=int(new_n)-int(n)
#     return cnt
# num_list=[]
# num_list.append(updown(n))
# num_list.append(downup(n))
# # print(num_list)
#
# for i in num_list:
#     if i==None:
#         continue
#     if i<min_result:
#         min_result=i
# print(min_result)