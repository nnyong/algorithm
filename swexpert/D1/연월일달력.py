import sys
sys.stdin=open('2056','r')

T=int(input())
for tc in range(1,T+1):
    data=input()
    year=data[0:4]
    month=data[4:6]
    day=data[6:8]
    result=False
    if int(month) in range(1,13):
        if int(month)%2:
            if int(day) in range(1,32):
                    result = True
        else:
            if int(month)==2:
                if int(day) in range(1, 29):
                    result = True
            else:
                if int(day) in range(1,31):
                    result = True
    if result:
        print('#{} {}'.format(tc,year + '/' + month + '/' + day))
    else:
        print('#{} {}'.format(tc,-1))