import sys,time
sys.stdin=open('파이프','r')
stime=time.time()

n=int(input())
pipe=[list(map(int,input().split())) for _ in range(n)]

def isSafe(y,x,i):
    if y < n and y >= 0 and x < n and y >= 0 and pipe[y][x] == 0:
        if i == 1:
            if pipe[y - 1][x] == 1 or pipe[y][x - 1] == 1:
                return False
        return True
    else:
        return False

def dfs(y,x,p=0):
    global cnt
    if y==0 and x==n-1:
        return
    if y==n-1 and x==n-1:
        cnt+=1
        return
    if p==0:
        if x == n - 1:
            return
        for i in range(2):
            if i==0:
                if isSafe(y,x+1,i):
                    dfs(y,x+1,i)
            else:
                if isSafe(y+1, x + 1,i):
                    dfs(y+1,x+1,i)
        return
    elif p==1:
        for i in range(3):
            if i==0:
                # if x == n - 1:
                #     return
                if isSafe(y, x + 1,i):
                    dfs(y,x+1,i)
            elif i==1:
                # if x == n - 1:
                #     return
                if isSafe(y+1, x + 1,i):
                    dfs(y+1,x+1,i)
            else:
                if isSafe(y + 1, x,i):
                    dfs(y + 1, x, i)
        return
    else:
        # if y == n - 1:
        #     return
        for i in range(1,3):
            if i==1:
                if isSafe(y+1, x + 1,i):
                    dfs(y+1,x+1,i)
            else:
                if isSafe(y + 1, x,i):
                    dfs(y + 1, x, i)
        return

cnt=0
dfs(0,1)
print(cnt)
print(time.time()-stime)