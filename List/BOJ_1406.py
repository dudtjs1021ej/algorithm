import sys
#백준 1406 시간 초과 뜸
'''
sentence = list(sys.stdin.readline().strip()) #공백제거된 리스트로 입력 받음
M = int(sys.stdin.readline()) #명령어 개수
cursor = len(sentence) #커서는 문장의 맨 뒤에 위치
stack = []

for _ in range(M):
    command = sys.stdin.readline().split()
    if command[0] == "L":
        if cursor != 0:
            cursor -= 1

    elif command[0] == "D":
        if cursor != len(sentence):
            cursor += 1

    
    elif command[0] == "B":
        if cursor != 0:
            del sentence[cursor-1]
            cursor -= 1


    elif command[0] == "P":
        #print("p="+command[2])
        sentence.insert(cursor, command[1])


for i in sentence:
    print(i, end='')
'''
#맞은 답
right_stack = []
left_stack = list(sys.stdin.readline().strip()) #공백제거된 리스트로 입력 받음
M = int(sys.stdin.readline()) #명령어 개수
for _ in range(M):
    command = sys.stdin.readline().split()
    if command[0] == "L":
        if left_stack:
            right_stack.append(left_stack.pop())

    elif command[0] == "D":
        if right_stack:
            left_stack.append(right_stack.pop())

    elif command[0] == "B":
        if left_stack:
            left_stack.pop()

    elif command[0] == "P":
        left_stack.append(command[1])

right_stack.reverse()
string = left_stack + right_stack
for i in string :
    print(i, end='')

