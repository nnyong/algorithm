data=[1, 8, 2, 5, 11, 1, 12, 2, 5, 6, 8, 4, 6, 9, 4, 15, 9, 10, 10, 11]
l = []
index = 0
for i in range(len(data)//2):
    bolt = []
    bolt.append(data[index])
    bolt.append(data[index+1])
    l.append(bolt)
    index+=2

print(l)
for n in range(len(l)):
    for key in range(len(l)):
        cnt = 0
        for i in range(len(l)):
            if key==i:
                continue
            else:
                if l[key][1]==l[i][0]:
                    if i<key:
                        temp=l[key]
                        for j in range(key-1,-1,-1):
                            l[j+1]=l[j]
                        l[0]=temp
                    else:
                        next=l[i]
                        l[i]=l[key+1]
                        l[key+1]=next
                    cnt=1
        if cnt==0:
            stop_index=key
            # key+1개
            for k in range(key+1):
                l.append(l[0])
                l.remove(l[0])
            break
print(l)