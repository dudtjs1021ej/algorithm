import sys
N = int(sys.stdin.readline())
result = 0
while True: #무한 루프
    if N % 5 == 0: #5kg봉지에 다 담아진다면 result 계산 후 break
        result += N // 5
        break

    N -= 3 #5kg봉지에 다 담을 수없다면 3키로 봉지에 하나 담음
    result += 1

    if N == 0 : #다 나눴다면 break
        break

    if N < 3: #딱 맞아떨어지지 않으면 result -1로 바꾼 후 break
        result = -1
        break

print(result)

    
