import sys
sys.stdin=open('슈퍼마리오','r')

score=[int(input()) for _ in range(10)]

index=0
next_index=False
for i in range(len(score)):
    if score[i]==100:
        result=score[i]
        index=i
        break
    elif score[i]<100:
        if i==9:
            index=i
            break
        score[i+1]=score[i]+score[i+1]
    elif score[i]>100:
        next_index=i
        break

if next_index:
    if score[next_index]-100<=100-score[next_index-1]:
        print(score[next_index])
    else:
        print(score[next_index-1])
else:
    print(score[index])
