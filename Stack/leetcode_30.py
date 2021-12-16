import sys
# 괄호 입력 값이 올바른지 판별하라
# (){}[]

def isValid(s):
    stack = []
    table = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    for char in s:
        if char not in table:
            stack.append(char)

        elif not stack or table[char] != stack.pop(): # 예외 처리와 일치 여부 판별
            return False

    return len(stack) == 0