# 4864문자열비교
import sys
sys.stdin=open('kmp.txt','r')

T=int(input())
for tc in range(1,T+1):
    str1=list(input())
    str2=list(input())
    # print(str1)
    # print(str2)

    pi=[0]*len(str1)
    pi[0]=-1
    pi[1]=0
    i=0
    j=1
    while j!=len(str1)-1:
        if str1[i]!=str1[j]:
            if i!=0:
                i=0
                if str1[i] == str1[j]:
                    p[j+1]=p[j]+1
                    j+=1
                    i+=1
                    break
            pi[j+1]=0
            j+=1
        else:
            pi[j+1]=pi[j]+1
            j+=1
            i+=1
    # print(pi)

    p=0
    result=0
    while p<len(str2)-len(str1)+1:
        k=0
        for i in range(len(str1)):
            if str1[i]==str2[p+i]:
                k+=1
            else:
                break
        if k==len(str1):
            result=1
            break
        p += k - pi[k]
    print('#{} {}'.format(tc,result))
