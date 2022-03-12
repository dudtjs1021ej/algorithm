# 창고 정리
# M회의 높이 조정을 마친 후 가장 높은곳과 가장 낮은 곳의 차이를 출력하세요.
import sys
n = int(input())
boxes = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    boxes.sort()
    # min = boxes.pop(0)
    # max = boxes.pop()
    # boxes.append(min+1) # min값
    # boxes.append(max-1) # max값
    boxes[0] += 1
    boxes[n-1] -= 1
boxes.sort()
print(boxes[n-1] - boxes[0])

# 후기
# 접근은 똑같이 했으나 굳이 pop, append 할필요없이 인덱스로 접근했으면 됐었다..
