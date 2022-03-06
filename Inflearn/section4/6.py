# A라는 지원자보다 키도 크고 몸무게도 무거운 지원자가 존재한다면 A지원자는 탈락입니 다.
import sys
n = int(input())
body = [list(map(int, input().split())) for _ in range(5)]
body.sort(reverse=True) # 키가 큰 순으로 내림차순 정렬
largest = 0
count = 0
for x, y in body:
    if y > largest:
        count += 1
        largest = y
print(count)

# 후기
# 이중포문 돌 필요없이 키 큰 순으로 정렬하고 최대 몸무게만 저장해서 비교하면 된다.

    