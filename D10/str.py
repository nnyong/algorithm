# 연습문제1 문자열 뒤집기

s='algorithm'
l=[]
for i in s:
    l.append(i)
length=len(l)
rep=length//2

for i in range(rep):
    l[i],l[length-1-i]=l[length-1-i],l[i]

new_s=''.join(l)
print(new_s)