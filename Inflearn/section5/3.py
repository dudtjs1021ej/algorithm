# 중위표기식이 입력되면 후위표기식으로 변환하는 프로그램을 작성하세요.
import sys
s = input()
stack = []
res = ''
for x in s:
    if x.isdecimal():
        res += x
    else:
        if x == '(':
            stack.append(x)

        elif x == '*' or x == '/': # 이전에 들어간 *나 /가 우선순위가 높기때문에 먼저 pop해서 출력
            while stack and ( stack[-1] == '*' or stack[-1] == '/'): 
                res += stack.pop()
            stack.append(x)

        elif x == '+' or x == '-': # x가 더하기나 빼기면 우선순위가 무조건 뒤이기때문에 스택에 있는애들 모두 pop
            while stack and stack[-1] != '(': # 여는 괄호 전까지 모두 pop
                res += stack.pop()
            stack.append(x)

        elif x == ')':
             while stack and stack[-1] != '(': 
                 res += stack.pop()
             stack.pop() # 괄호 출력 안함

while stack: # 스택에 남아있는거 다 출력
    res += stack.pop()
print(res)

# 후기
# 후위연산자 구현하는 방법 외워두자
# 숫자는 무조건 출력 / 우선순위가 높은 연산자 먼저 출력
# +-면 스택에 있는 연산자가 무조건 높기때문에 괄호( 전 까지 다빼서 출력
# */면 스택 안에 있는 */가 우선순위가 높기때문에 얘네만 뺴서 출력
# 모든 식 다 계산했으면 스택에 남은 애들 출력