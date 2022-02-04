# k번째 수
import sys
T = int(input())

# 내 풀이
for T in range(1,T+1):
    N, s, e, k = map(int,input().split())
    test_case = list(map(int, input().split()))
    sort_test_case = test_case[s-1:e]
    sort_test_case.sort()
    print(T, sort_test_case[k-1])

# 답
for t in range(T):
    N, s, e, k = map(int,input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()
    print("#%d %d"%(T+1, a[k-1]))
    

# 후기
'''
잘못 접근 한 점
1. 처음에 인덱스를 잘못 생각해서 a[s+1:e+2] 로 풀이
2. a[s-1:e].sort() 로 풀었다가 에러 (파이썬이라 되겠지란 마음으로 해봄,,)
3. print # 안함 
'''
