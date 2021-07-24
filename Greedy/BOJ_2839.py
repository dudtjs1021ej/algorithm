import sys
N = int(sys.stdin.readline())
result = 0
while True:
   
    if N % 5 == 0:
        result += N // 5
        break
    N -= 3 #5kg봉지에 다 담을 수없다면 3키로 봉지에 하나 담음
    result += 1
    if N == 0 :
        break

    if N < 3:
        result = -1
        break

print(result)

    
