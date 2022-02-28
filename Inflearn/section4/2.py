# 만들 수 있는 최대 랜선의 길이를 구하는 프로그램을 작성하시오.
# N개보다 많이 만드는 것도 N개를 만드는 것에 포함된다. (N개이상)
import sys
# 랜선길이를 (1~ 제일 긴 길이)로 하고 가운데값이랑 비교하며 길이를 이분탐색으로 찾는다.
def mySolution():
    k, n = map(int, input().split())
    a = [int(input()) for _ in range(k)]
    left = 1
    right = max(a)
    answer = -2147000000
    while left <= right:
        sum = 0 # 만들 수 있는 끈의 개수
        mid = (left+right) // 2
        for i in range(k):
            sum += a[i] // mid
        if sum < n:
            right = mid-1
        elif sum >= n:
            answer = mid
            left = mid+1
    print(answer)

def answer():
    # 그 길이로 만들 수 있는 끈의 개수 리턴
     def Count(len):
        cnt = 0
        for x in Line:
            cnt += (x//len)
        return cnt

     k, n = map(int, input().split())
     Line = []
     res = 0
     largest = 0
     for i in range(k):
         tmp = int(input())
         Line.append(tmp)
         largest = max(tmp, largest)
        
     lt = 0
     rt = largest
     while lt<=rt:
         mid = (lt+rt) // 2
         if Count(mid) >= n:
             res = mid
             lt = mid + 1
         else:
             rt = mid - 1

# 후기
# 어떻게 풀지 몰라서 풀이 설명 듣고 코드 짬.
# 이분탐색으로 풀이 -> 1~최대길이에서 끈의 길이가 n개 이상 되게 범위 반으로 줄여가며 이분 탐색
# 개인적으로 내 풀이가 더 나은듯..



