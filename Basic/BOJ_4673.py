import sys
# 셀프 넘버 출력하기
num = set(range(1,10001))
transNum = set()

for i in num:
    for j in str(i): #각자리 수 더하기
        i += int(j)
    transNum.add(i)

selfNum = sorted(num - transNum)
for i in selfNum:
    print(i)