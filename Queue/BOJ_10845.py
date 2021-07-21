import sys
queue = []
def push(x):
    queue.append(x)

def pop():
    return -1 if not queue else queue.pop(0)

def size():
    return len(queue)

def empty():
    return 1 if not queue else 0

def front():
    return -1 if not queue else queue[0]

def back():
    return -1 if not queue else queue[-1]


N = int(sys.stdin.readline())
#N = int(input()) -> 시간초과

for _ in range(N):
    command = sys.stdin.readline().split() 
    if command[0] == "push":
        push(command[1])

    elif command[0] == "pop":
        print(pop())

    elif command[0] == "size":
        print(size())

    elif command[0] == "empty":
        print(empty())

    elif command[0] == "front":
        print(front())

    elif command[0] == "back":
        print(back())