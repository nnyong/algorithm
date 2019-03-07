import sys
sys.stdin=open('의석이.txt','r')

T=int(input())
for tc in range(1,T+1):
    data=[list(input()) for i in range(5)]
    # print(data)
    max_len=0
    for i in data:
        if len(i)>=max_len:
            max_len=len(i)
    map=[[0]*max_len for i in range(5)]
    for y in range(5):
        for x in range(max_len):
            if x>len(data[y])-1:
                continue
            map[y][x]=data[y][x]
    # print(map)
    string=''
    for x in range(max_len):
        for y in range(5):
            if map[y][x]==0:
                continue
            string+=map[y][x]
    print('#{} {}'.format(tc,string))