# 문자와 숫자가 섞여있는 문자열이 주어지면 그 중 숫자만 추출하여 그 순서대로 자연수를 만 듭니다. 
# 만들어진 자연수와 그 자연수의 약수 개수를 출력합니다.
import sys
s = input()
num = 0
count = 0 # 약수 개수
for x in s:
    if x.isdecimal():
        print(x)
        num = num*10 + int(x)

for i in range(1,num+1):
    if num % i == 0:
        count += 1
print(num)
print(count)

# 후기
# 풀이와 똑같이 품.
# isdecimal() -> 0~9의 숫자인지 체크해주는 내장 함수
