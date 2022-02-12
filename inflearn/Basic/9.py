#1에서부터 6까지의 눈을 가진 3개의 주사위를 던져서 다음과 같은 규칙에 따라 상금을 받는 게임이 있다.
#규칙(1) 같은 눈이 3개가 나오면 10,000원+(같은 눈)*1,000원의 상금을 받게 된다. 
# 규칙(2) 같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)*100원의 상금을 받게 된다. 
# 규칙(3) 모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)*100원의 상금을 받게 된다.
import sys
def mySoultion():
    n = int(input())
    results = [] # 계산 결과 값들

    for _ in range(n):
        numbers = list(map(int, input().split()))
        max_count = -2147000000 # 같은숫자 개수
        value = -1 # 많이 나온 숫자
        result = 0

        for i in numbers:
            count = numbers.count(i) # 해당 숫자의 count
            if max_count < count:
                max_count = count
                value = i

        if max_count == 3:
            result = 10000 + value * 1000
        elif max_count == 2:
            result = 1000 + value * 100
        elif max_count == 1:
            result = max(numbers) * 100
        results.append(result)
    print(max(results))

def answer():
    result = 0
    n = int(input())
    for _ in range(3):
        tmp = input().split()
        tmp.sort()
        a, b, c = map(int, tmp)
        if a==b and b==c:
            money = 10000 + a*1000
        elif a==b or a==c:
            money = 1000 + a*100
        elif b==c:
            money = 1000 + b*100
        else:
            money = c*100
        if result < money:
            result = money
    print(result)

answer()

# 후기
# 잘못 푼 점
# 굳이 for문으로 나온 주사위수를 count할 필요 없이 
# 정렬한 후 a,b,c로 세 수를 빼서 if문으로 비교하면 된다.

    
            

