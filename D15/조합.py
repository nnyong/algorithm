visited = [0] * 6
def Get(k,s):
    if len(s)==3:
        print(s)
        return
    if k > 5:
        return
    visited[k] = 1
    Get(k+1,s+str(k))
    visited[k] = 0
    Get(k+1,s)
Get(1,'')