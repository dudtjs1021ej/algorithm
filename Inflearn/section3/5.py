# N개의 수로 된 수열 A[1], A[2], ..., A[N] 이 있다. 
# 이 수열의 i번째 수부터 j번째 수까지의 합 A[i]+A[i+1]+...+A[j-1]+A[j]가 
# M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
import sys
def mySoultion():
    n, m =map(int, input().split())
    a = list(map(int, input().split()))
    count = 0 # 경우의 수 
    for index, value in enumerate(a):
        if a[index] == m: # 현재값이 m이면 count추가하고 넘어감
            count += 1
            continue
        p = 1
        sum = a[index]
        # m보다 작을때까지 sum과 비교하며 다음 값 더함
        while p+index < n and sum < m:
            sum += a[index+p]
            p += 1
            if sum == m:
                count += 1
                break
    print(count)

# lt, rt 두 포인터를 두고 lt~rt-1까지 더하며 전진하며 풀이
def answer():
    n, m =map(int, input().split())
    a = list(map(int, input().split()))
    lt = 0
    rt = 1
    tot = a[0] # lt~ rt-1 까지 더한 값
    cnt = 0
    while True:
        if tot < m: 
            if rt < n:
                tot += a[rt]
                rt += 1
            else:
                break
        elif tot == m:
            cnt += 1
            tot -= a[lt]
            lt += 1
        else: # m보다 클 때
            tot -= a[lt]
            lt += 1
# 후기
# 투 포인터로 푸는 방법을 배움.

