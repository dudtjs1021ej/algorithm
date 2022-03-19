# 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때, 
# 잘려진 쇠막대기 조각의 총 개수를 구하는 프로그램을 작성하시오.
import sys
s = input()
stack = []
sum = 0
for i in range(len(s)):
    if s[i] == "(":
        stack.append(s[i])
    else: # )일 때 
        stack.pop()
        if s[i-1] == "(": # 레이저일 때
            sum += len(stack)
        else: # )일 때 -> 막대기 닫는 지점일 때
            sum += 1
           
print(sum)

# 후기
# 처음에 모든 괄호를 한번에 스택에 넣는것으로 잘못 접근함
# 괄호 하나하나 스택에 넣어가며 넣는 값이 ) 일 때, pop 하게 풀이



