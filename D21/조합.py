nn = 5
rr = 3
IsUsed= [0]*(rr+1)
def GetSome(n , r):
    if r > rr :
        for i in range(1, rr+1):
              print(IsUsed[i], end=' ')
        print()
        return
    if n > nn : return
    IsUsed[r] = n
    GetSome(n+1, r+1)
    GetSome(n + 1, r)



GetSome(1,1)