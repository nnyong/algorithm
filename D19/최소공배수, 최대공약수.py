number1=24
number2=18

def gcd(n1,n2):
    while n2!=0:
        r=n1%n2
        n1=n2
        n2=r
    return n1

def lmd(n1,n2):
    return (n1*n2)//gcd(n1,n2)

if number1>=number2:
    print(gcd(number1,number2))
    print(lmd(number1, number2))
else:
    print(gcd(number2, number1))
    print(lmd(number2,number1))