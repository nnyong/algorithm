import sys
sys.stdin=open('지능형기차','r')

data=[list(map(int,input().split())) for _ in range(4)]
# print(data)
people=0
for d in data:
    on=d[0]
    off=d[1]
    if people<people+off-on:
        people+=off-on
print(people)