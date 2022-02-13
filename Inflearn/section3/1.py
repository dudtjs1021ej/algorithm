# N개의 문자열 데이터를 입력받아 앞에서 읽을 때나 뒤에서 읽을 때나 같은 경우(회문 문자열) 이면 
# YES를 출력하고 회문 문자열이 아니면 NO를 출력하는 프로그램을 작성한다.
import sys
# 맨앞은 start, 맨뒤는 end로 같은지 검사하며 한칸씩 이동
def mySoultion():
    n = int(input())
    for _ in range(n):
        word = input()
        word = word.lower() # 모두 소문자로 변환
        start = 0
        end = len(word) - 1
        while start < end:
            if start == (len(word) // 2 - 1) and word[start] == word[end]: # start가 반까지 검사했다면
                print("YES")
                break

            elif word[start] == word[end]: # start, end 한칸씩 바꿔주며 검사
                start += 1
                end -= 1
            else:
                print("NO")
                break

def answer():
    n = int(input())
    for i in range(n):
        s = input()
        s = s.upper()
        size = len(s)
        for j in range(size//2):
            if s[j] != s[-1-j]:
                print("#%d NO"%(i+1))
                break
        else: #for문의 else (break 안당한 경우)
            print("#%d YES"%(i+1))

# 후기
"""
잘못푼점
print문 제대로 안봐서 잘못 출력함.

새로배운점
인덱스 -1로 접근 가능함.
for문의 else 사용가능
"""

