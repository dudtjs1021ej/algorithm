import sys
n = int(sys.stdin.readline())
for _ in range(n):
    case = list(map(int, sys.stdin.readline().split()))
    avg = sum(case[1:]) / case[0]
    count = 0 
    for i in case[1:]:
        if i > avg:
            count += 1
    result = count / case[0] * 100
    print("%.3f"%result+"%")