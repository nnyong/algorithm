def power1(a,b): #O(n)
    if b==0: return 1
    elif b==1: return a
    else: return a*power2(a,b-1)

def power2(a, b): #O(logn)
    if b==0: return 1
    elif b==1: return a
    elif b&1: return a*power1(a,b-1)
    else:
        temp=power2(a,b//2)
        return temp*temp

def power3(a,b): #O(logn)
    ans=1
    while b>0:
        if b&1: ans*=a  #b가 홀수이면ff
        a=a*a
        b//=2
    return ans

print(power1(2,900))
print(power2(2,40000))
print(power3(2,40000))