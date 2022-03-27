# 이번에는 N개의 단어를 노트에 적었는데 시에 쓰지 않은 단어가 하나 있다고 합니다. 
# 여러분이 찾아 주세요.
import sys
n = int(input())
words = dict() # 딕셔너리 -> key는 word / vlaue는 0 또는 1
for _ in range(n):
    word = input()
    words[word] = 1

for _ in range(n-1):
    word = input()
    words[word] = 0

for key, value in words.items():
    if value == 1:
        print(key)
        break

# 후기
# 이중포문쓰면서 각각의 값을 비교하는 걸로 풀었으나 
# 딕셔너리에 key값을 단어로 넣으면 간단하게 풀 수 있었음

