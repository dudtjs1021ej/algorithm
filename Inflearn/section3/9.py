# 지도 정보가 N*N 격자판에 주어집니다. 
# 각 격자에는 그 지역의 높이가 쓰여있습니다. 
# 각 격자 판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다. 
# 봉우리 지역이 몇 개 있는 지 알아내는 프로그램을 작성하세요.
# 격자의 가장자리는 0으로 초기화 되었다고 가정한다.
import sys

def mySolution():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    count = 0

    # 가장자리 0 넣음 -> edge 변수로 넣으면 참조되어서 0 두번 더해짐
    # edge = [0]* n
    # a.append(edge)
    # a.insert(0, edge)

    a.append([0]*n)
    a.insert(0, [0]*n)

    for x in a:
        x.append(0)
        x.insert(0,0)

    for i in range(1, n+1):
        for j in range(1, n+1):
            num = a[i][j]
            # 상하좌우보다 더 크면 봉우리
            if num > a[i-1][j] and num > a[i+1][j] and \
            num > a[i][j-1] and num > a[i][j+1]:
                count += 1
    print(count)

def answer():
    dx = [-1,0,1,0] # 좌우상하
    dy = [0,1,0,-1]
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    count = 0

    a.append([0]*n)
    a.insert(0, [0]*n)

    for x in a:
        x.append(0)
        x.insert(0,0)

    for i in range(1, n+1):
        for j in range(1, n+1):
            if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
                count += 1
    print(count)

answer()

# 후기
# edge 리스트를 따로 두고 앞뒤로 붙였더니 값이 참조되어서 헤맸음.
# 새로 배운 것 
#   if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
#   -> all() 함수 = 모든 조건 만족하면 참 / if문안에서 for문 돌기