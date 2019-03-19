import sys
sys.stdin=open('암호코드스캔.txt','r')

T=int(input())
for tc in range(1,T+1):
    print('#{}'.format(tc))
    row,col=map(int,input().split())
    print(row,col)
    data=[]
    for i in range(row):
        data.append(input())
    print(data)
    pw_list=[]
    for i in data:
        if i=='0'*col:
            continue
        else:
            if i not in pw_list:
                pw_list.append(i)
    print(pw_list)

    for pw in range(len(pw_list)):
        for i in range(col-1,-1,-1):
            if pw_list[pw][i]!='0':
                pw_list[pw]=pw_list[pw][:i+1]
                break
    print(pw_list)

    dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    pw_2=[]
    for pw in range(len(pw_list)):
        temp= ''
        for i in range(len(pw_list[pw])-1,-1,-1):
            if pw_list[pw][i].isnumeric():
                for r in range(4):
                    if int(pw_list[pw][i])&(1<<r):
                        temp='1'+temp
                    else:
                        temp = '0' + temp
            else:
                for r in range(4):
                    if dict[pw_list[pw][i]]&(1<<r):
                        temp='1'+temp
                    else:
                        temp = '0' + temp
        pw_2.append(temp)
    print(pw_2)
    for pw in range(len(pw_2)):
        for i in range(len(pw_2[pw])-1,-1,-1):
            if pw_2[pw][i]=='1':
                pw_2[pw]=pw_2[pw][:i+1]
                break
    print(pw_2)

    pw_dict={'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,'0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}
    for pw in range(len(pw_2)):
        for i in range(len(pw_2[pw]) - 1, -1, -1):
            for pd in pw_dict.keys():
                if pw_2[pw][i-6:i+1]==pd:
                    pw_2[pw]=pw_2[pw][i-55:i+1]
                    break
                else:
            break
    print(pw_2)