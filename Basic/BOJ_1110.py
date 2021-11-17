import sys
n =int(sys.stdin.readline())
calcN = n
count = 0
while(True) :
    if (count!=0 and calcN == n):
        break
    if calcN < 10:
        calcN = calcN*10 + calcN
        count = count + 1
        continue

    firstN = calcN % 10
    secondN = calcN // 10
    plusN = firstN + secondN #각자리수의 합
    calcN = 10*firstN + plusN % 10
    count = count + 1

print(count)


