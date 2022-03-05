# 한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들 려고 한다. 
# 각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고, 
# 각 회의가 겹치지 않게 하 면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라.
import sys
n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s,e)) # 튜플

# 끝나는 시간으로 정렬 (x[1]이 우선순위로 정렬, x[1]이 같으면 x[0]으로 정렬)   
meeting.sort(key=lambda x: (x[1], x[0])) 

et = 0
count = 0
for s, e in meeting:
    if s >= et:
        et = e
        count += 1
print(count)

# 후기
# 시작시간으로 정렬해서 풀었는데 끝나는 시간으로 정렬하면 간단한 문제였다.
