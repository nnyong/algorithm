# 반복문자 지우기
import sys
sys.stdin=open('4873.txt','r')

T=int(input())

for tc in range(1,T+1):
    s=input()
    # print(s)

    top=-1
    new_s=[]
    for i in range(len(s)):
        if new_s==[]:
            new_s.append(s[i])
            top+=1
        else:
            if s[i]==new_s[top]:
                new_s.pop()
                top-=1
            else:
                new_s.append(s[i])
                top+=1

    print(f'#{tc} {len(new_s)}')