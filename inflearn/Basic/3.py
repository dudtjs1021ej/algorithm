# k번째 큰 수
# 중복일수도 있는 카드 N장중에 3장을 뽑아서 더한값 중 K번째로 큰 값을 찾아라.
import sys

# --내 풀이--
def mySolution():
    n, k = map(int,input().split())
    # 중복 제거를 위해 리스트 -> 셋 -> 리스트
    card = list(map(int, input().split()))
    card = set(card) 
    card = list(card)
    sums = set() # 합들을 더할 집합 sums

    for i in range(len(card)):
        sum = 0
        sum = card[i]
        start = i+1
        for j in range(start, len(card)):
            for m in range(j+1, len(card)):   
                sum += card[j]
                sum += card[m]
                sums.add(sum)
                sum = card[i]
                # sum = 0 -> 여기서 틀림
        
    sums = list(sums) # 중복제거를 위해 set으로 선언했다가 인덱스로 접근하기 위해 리스트 타입 변경
    sums.sort()
    print(sums[len(sums)-k+1])

# --답--
def Answer():
    n, k = map(int,input().split())
    a = list(map(int, input().split()))
    res = set()
    for i in range(n):
        for j in range(i+1,n):
            for m in range(j+1, n):
                res.add(a[i]+a[j]+a[m])

    res = list(res)
    res.sort(reverse=True) # 내림차순 정렬
    print(res[k-1])

mySolution()

# --후기--
'''
잘못 푼 점
1. sum 초기화를 이상한데에서 해서 헤맸다.
2. 변수이름 k를 두번이나 썼다.. (이거땜에 엄청 헤맴)
3. i도는 for문에 왜 연산을 했을까.. + sum 변수가 필요 없었다.

새로 배운 것
1. 내림차순 정렬 : res.sort(reverse=True)
2. 집합 set은 중복 불가, set.add() 로 사용
'''