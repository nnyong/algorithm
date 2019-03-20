# 5c3
data=[1,2,3,4,5]

# 조합
l=[]
for a in range(len(data)):
    for b in range(a+1,len(data)):
        for c in range(b+1,len(data)):
            l.append((data[a],data[b],data[c]))
print(l)

# 중복조합
l=[]
for a in range(len(data)):
    for b in range(a,len(data)):
        for c in range(b,len(data)):
            l.append((data[a],data[b],data[c]))
print(l)