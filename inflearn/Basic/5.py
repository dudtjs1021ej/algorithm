# 정다면체
# 두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확 률이 높은 숫자를 출력하는 프로그램을 작성하세요.
# 정답이 여러 개일 경우 오름차순으로 출력합니다.
import sys

# 딕셔너리 key엔 합, value엔 그 합의 개수를 넣어서 풀었음
def mySolution():
    n, m = map(int, input().split())
    dict = {}
    for i in range(1, n+1):
        for j in range(1, m+1):
            sum = i+j
            if sum in dict: # 이미 합이 딕셔너리에 있다면
                dict[sum] += 1
            else:
                dict[sum] = 1

    sorted_value = sorted(dict.values(), reverse=True) # value를 기준으로 오름차순 정렬
    max_percent = sorted_value[0] # 가장 높은 횟수
    for key, value in dict.items():
        if value == max_percent:
            print(key, end=" ")

def answer():
    # 리스트의 인덱스가 합, 값이 그 합의 개수로 풀었음
    n, m = map(int, input().split())
    cnt = [0]*(n+m+3) #n+m+3개 초기화 
    max = -2147000000
    for i in range(1, n+1):
        for j in range(1, m+1):
            cnt[j+j] += 1

    for i in range(n+m+1):
        if max < cnt[i]:
            max = cnt[i]

    for i in range(n+m+1):
        if cnt[i] == max:
            print(cnt[i], end=' ')
        
# 후기
# 잘못 푼 점
'''
1. 굳이 딕셔너리로 안풀어도 됐었다. (리스트로 미리 개수만큼 초기화시켜 사용하면 가능)
2. 최대값, 최소값 구하는걸 자꾸 정렬해서 푼다.
'''
