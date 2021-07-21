import sys
stack = []
#push함수 : x를 스택에 넣음
def push(x):
    stack.append(x)

#pop함수 : 가장 위의 정수를 pop해서 리턴
def pop():
    return -1 if len(stack) == 0 else stack.pop()

#size 함수 : 스택의 정수 개수 리턴
def size():
    return len(stack)

#empty함수 : 비어있으면 1리턴 아니면 0리턴
def empty():
    return 1 if len(stack) == 0 else 0 

#top함수 : 스택 가장 위의 정수 리턴
def top():
    return stack[-1] if stack else -1

N = int(sys.stdin.readline()) #시간 단축을 위해 input()대신 씀
for _ in range(N):
    command = sys.stdin.readline().split() #명령어 split
    if command[0] == "push":
        push(command[1])

    elif command[0] == "pop":
        print(pop())

    elif command[0] == "size":
        print(size())

    elif command[0] == "empty":
        print(empty())

    elif command[0] == "top":
        print(top())
