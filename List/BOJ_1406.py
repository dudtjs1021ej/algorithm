import sys
sentence = list(sys.stdin.readline().strip()) #리스트로 입력 받음
M = int(sys.stdin.readline()) #명령어 개수
cursor = len(sentence) #커서는 문장의 맨 뒤에 위치

for _ in range(M):
    command = sys.stdin.readline().strip()
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
        sentence.insert(cursor, command[2])


for i in sentence:
    print(i, end='')