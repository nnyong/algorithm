# ladder 재귀
import sys
sys.stdin=open('ladder.txt','r')
l=[]
for i in range(10):
    l.append(list(map(int,input().split())))
print(l)

# def DFS(here):
#     print(here)
#     visited[here]=True
#
#     for next in range(10):
#         if MyMap[here][next] and not visited[next]:
#             DFS(next)

# goal=l[next][here]
def Ladder(up,here):
    for next in range(up-1,0,-1):
        if l[next][here-1]==1 or l[next][here+1]==1:
            if l[next][here-1]==1:
                l_next=next
                l_here=here-1
                while l[l_next][l_here]!=0:
                    l_here-=1
                here=l_here+1
                up=l_next
                Ladder(up,here)
            else:
                r_next=next
                r_here=here+1
                while l[r_next][r_here]!=0:
                    r_here+=1
                here=r_here-1
                up=r_next
                Ladder(up,here)
    print(up)
    print(here)

Ladder(9,6)







