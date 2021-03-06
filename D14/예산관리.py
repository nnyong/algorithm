# 예산 관리
# 샬랄라는 예산이 많은 부서에서 일하고 있다. 연말이 가까워지면서 부서의
# 예산을 가급적 모두 집행해야 될 상황이 되었다.
# 샬랄라는 예산 범위를 넘지 않는 선에서 다양한 활동을 하고 싶어 한다.
# 지금 남은 예산(B)이 40이고(단위:만원), 예산을 사용할 수 있는 활동(n)이 6개가 있다.
# 6개의 활동에 각각 드는 비용은 7, 13, 17, 19, 29, 31이다. 여기서 40을 채울 수
# 있는 활동의 개수는 상관이 없다. 40을 넘지 않는 범위에서 활동 비용을 조합해보면,
# 7 + 13 + 17 = 37
# 7 + 31 = 38
# 7 + 13 + 19 = 39
# ...
# 따라서 40을 초과하지 않으면서 예산을 최대로 사용할 수 있는 비용은 39이다.
# 샬랄라를 도와 줄 수 있는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 남은 예산(B)이 입력된다. ( 10 <= B <= 35,000 )
# 둘째 줄에 예산을 사용할 수 있는 활동의 수(n)가 입력된다. (1 <= n <= 21 )
# 셋째 줄에 공백을 기준으로 n개의 활동비가 양의 정수로 입력된다.
# 출력
# 남은 예산을 초과하지 않으면서 최대로 사용할 수 있는 비용액을 출력한다.
# 입력 예 				출력 예
# 40				39
# 6
# 7 13 17 19 29 31

import sys
sys.stdin=open('예산관리.txt','r')

B=int(input())
n=int(input())
b=list(map(int,input().split()))

max_budget=0
visited=[0]*n
def getSome(k,budget):
    global max_budget
    if budget<=B:
        if budget>max_budget:
            max_budget=budget
    if budget>B or k>=n:
        return
    visited[k]=1
    getSome(k+1,budget+b[k])
    visited[k]=0
    getSome(k + 1, budget)

getSome(0,0)
print(max_budget)

