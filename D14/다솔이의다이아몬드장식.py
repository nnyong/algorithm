import sys
sys.stdin=open('다솔이.txt','r')
n=int(input())
for tc in range(1,n+1):
    string=input()
    if len(string)==1:
        dia=[[0]*5 for i in range(5)]
        for y in range(5):
            if y==0 or y==4:
                dia[y]=['.','.','#','.','.']
            elif y==1 or y==3:
                dia[y]=['.','#','.','#','.']
            else:
                dia[y]=['#','.',string,'.','#']
        for j in dia:
            for k in j:
                print(k,end='')
            print()
    else:
        dia=[[0]*(5+4*(len(string)-1)) for i in range(5)]
        i = 0
        for y in range(5):
            for x in range(0,len(dia[0])-1,4):
                if y==0 or y==4:
                    dia[y][x:x+5]=['.','.','#','.','.']
                elif y==1 or y==3:
                    dia[y][x:x+5]=['.','#','.','#','.']
                else:
                    dia[y][x:x + 5]=['#', '.', string[i], '.', '#']
                    i+=1
        for j in dia:
            for k in j:
                print(k,end='')
            print()

