# ladder 비재귀
import sys
sys.stdin=open('ladder.txt','r')

for tc in range(10):
    tc=int(input())
    ladder=[]
    for i in range(100):
        ladder.append(list(map(int,input().split())))
    print('# {}'.format(tc))
    print(ladder)