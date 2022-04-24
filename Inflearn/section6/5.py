# C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
# N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 철수가 트럭에 태울 수 있는 가장 무거운 무게를 구하는 프로그램을 작성하세요.

import sys
def DFS(index, sum, total_sum):
    global result # 전역변수
    if sum + (total-total_sum) < result: # time cut
        return
    if sum > c: # time cut
        return

    if index == n:
        if sum > result:
            result = sum
    else:
        DFS(index+1, sum+a[index], total_sum+a[index])
        DFS(index+1, sum, total_sum+a[index])


if __name__ == "__main__":
    result = -2147000000
    c, n = map(int, input().split())
    a = []
    for _ in range(n):
        num = int(input())
        a.append(num)
    total = sum(a)
    DFS(0,0,0)
    print(result)

# 앞에 부분집합 문제와 같은 풀이
# sum 최대값 DFS함수 안에서 바로 비교 o