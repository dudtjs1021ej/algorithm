import sys
#풀이1(내가 푼 것) -> 매번 대기시간 젤 작은 사람 찾아서 더 함
'''
num = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split())) 
sumTimes = 0
waitTimes = []
for _ in range(num):
    sumTimes += min(p) #가장 대기시간이 적은 사람 먼저 더함
    waitTimes.append(sumTimes)
    p.remove(min(p)) #가장 대기시간이 적은 사람 삭제

print(sum(waitTimes))
'''

#풀이2 -> 처음부터 오름차순으로 대기시간 정렬 후 차례대로 더함 
num = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split())) 
p.sort()
sumTimes = 0
waitTimes = []
for i in p:
    sumTimes += i
    waitTimes.append(sumTimes)

print(sum(waitTimes))