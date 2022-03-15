# n과 1부터 n까지의 수를 사용하여 이루어진 수열의 역수열이 주어졌을 때, 
# 원래의 수열을 출 력하는 프로그램을 작성하세요.
import sys
n = int(input())
a = list(map(int, input().split()))
seq = [0]*n
for i in range(n):
    count = 0
    for j in range(n):
        if  a[i] == 0 and seq[j] == 0:
            seq[j] = i+1
            break

        if seq[j] == 0:
            a[i] -= 1
for x in seq:
    print(x, end=' ')
        
# 풀이
# 오름차순으로 빈자리 개수 체크 -> seq에 비어있으면 0, 아니면 해당숫자 넣음
# 이전에 seq에 넣은 숫자는 이미 나보다 작은것이기때문에 무시 가능

# 후기
# 어떻게 풀지 감이 안와서 풀이보고 코드짬
# else: continue를 넣었는데 넣을 필요가 없었음
