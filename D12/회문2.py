import sys
sys.stdin=open('회문2.txt','r')

for tc in range(10):
    tc=int(input())
    data=[list(input()) for i in range(100)]
    # print(data)

    result=[]
    for m in range(2,100):
        center = m // 2
        for y in range(100):
            r_center = m // 2
            while r_center <= center + (100 - m):
                if m % 2:
                    a = r_center - 1
                    b = r_center + 1
                else:
                    a = r_center - 1
                    b = r_center
                cnt = 0
                for r in range(m // 2):
                    if data[y][a] == data[y][b]:
                        a -= 1
                        b += 1
                        cnt += 1
                    else:
                        break
                r_center += 1
                l=[]
                if cnt == center:
                    for i in range(m):
                        l.append(data[y][a + 1])
                        a += 1
                    result.append(l)

        for x in range(100):
            c_center = m // 2
            while c_center <= center + (100 - m):
                if m % 2:
                    a = c_center - 1
                    b = c_center + 1
                else:
                    a = c_center - 1
                    b = c_center
                cnt = 0
                for c in range(m // 2):
                    if data[a][x] == data[b][x]:
                        a -= 1
                        b += 1
                        cnt += 1
                    else:
                        break
                c_center += 1
                l=[]
                if cnt == center:
                    for i in range(m):
                        l.append(data[a+1][x])
                        a += 1
                    result.append(l)

    max_len = 1
    for i in result:
        if len(i) > max_len:
            max_len = len(i)
    print('#{} {}'.format(tc,max_len))
