# 구간 [a, b] (단, 1 ≤ a ≤ b ≤ 20)가 주어지면 
# 위치 a부터 위치 b까지의 카드를 현재의 역순으로 놓는다.
import sys

# 범위의 맨앞과 맨끝을 swap하며 전진하는 방식
def mySoultion():
    cards = []
    for i in range(1,21):
        cards.append(i)

    for _ in range(10):
        a, b = map(int, input().split())
        count = b-a+1 # 카드의 개수
        # 범위 맨 앞과 맨 끝 swap 하며 전진
        for i in range(count//2): 
            cards[a-1+i], cards[b-1-i] = cards[b-1-i], cards[a-1+i]
    for i in cards:
        print(i, end=' ')

def answer():
    a = list(range(21)) # 0~20
    for _ in range(1):
        s, e = map(int, input().split())
        for i in range((e-s+1) // 2):
            a[s+i], a[e-i] = a[e-i], a[s+i]
    
    a.pop(0) # 0 pop
    for i in a:
        print(i, end=' ')

# 후기
# 거의 똑같이 풀었지만 0~20 으로 푼 뒤 맨 앞만 pop해주는 방식은 생각하지 못함


