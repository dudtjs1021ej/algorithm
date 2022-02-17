# 오름차순으로 정렬이 된 두 리스트가 주어지면 
# 두 리스트를 오름차순으로 합쳐 출력하는 프로 그램을 작성하세요.
import sys
# 각 리스트의 맨 앞 값 비교하며 새로운 리스트에 append
def mySolution():
    result = []
    n = int(input())
    list1 = list(map(int, input().split()))
    m = int(input())
    list2 = list(map(int, input().split()))
    while True:
        # 한쪽 리스트가 비어있으면 다른쪽 리스트 다 append
        if not list1:
            for i in list2:
                result.append(i)
            break
        elif not list2:
            for i in list1:
                result.append(i)
            break

        # 각 리스트의 맨 앞 값을 비교해서 append
        elif list1[0] <= list2[0]:
            result.append(list1.pop(0))
        else:
            result.append(list2.pop(0))
    
    for i in result:
        print(i, end=' ')

def answer():
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    p1 = p2 = 0
    c = []
    while p1<n and p2<m:
        if a[p1] <= b[p2]:
            c.append(a[p1])
            p1 += 1
        else:
            c.append(b[p2])
            p2 += 1
    if p1<n:
        c += a[p1:]
    if p2<m:
        c += b[p2:]
    for i in c:
        print(i, end=' ')

# 후기
# 다르게 푼 점
# 1. for문을 돌 필요없이 슬라이싱을 사용(a[p1:])해서 바로 남은 값 넣을 수 있음
# 2. while문 끝나고 남은 값 넣어도 됨

