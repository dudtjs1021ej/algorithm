import sys
#1316 그룹 단어 체커
N = int(sys.stdin.readline())
result = N
for _ in range(N):
    word = sys.stdin.readline()
    for i in range(len(word)-1):
        if word[i] != word[i+1]: #앞뒤 알파벳이 다른 알파벳일 경우
            if word[i+1] in word[:i]: #뒤쪽에 뒷 알파벳이 포함 되어있는지 체크
                result -= 1
                break
            

print(result)