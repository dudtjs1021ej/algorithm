import sys
s = input()
stack = []
for x in s:
    if x.isdecimal():
        # stack.append(x)
        stack.append(int(x))
    else:
        # b = int(stack.pop())
        # a = int(stack.pop())
        b = stack.pop()
        a = stack.pop()
        if x == "*":
            c = a*b
        elif x == "/":
            c = a/b
        elif x == "+":
            c = a+b
        elif x == "-":
            c = a-b
        stack.append(c)       
print(stack.pop())
        
# 후기
# stack에 넣을때 int형으로 바꾸고 append하는것 제외하고 동일하게 품