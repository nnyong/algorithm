import sys

sys.stdin = open('permutation.txt', 'r')

Data = list(map(int, input().split()))

print(Data)

cand1=0
for i in range(len(Data)-1):
    if Data[i]<Data[i+1]:
        cand1=i

cand2=len(Data)-1
while Data[cand1]>Data[cand2]:
    cand2-=1

Data[cand1],Data[cand2]=Data[cand2],Data[cand1]
Data[cand1+1:]=Data[:cand1:-1]
print(Data)