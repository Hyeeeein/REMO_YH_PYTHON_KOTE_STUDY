from collections import deque
import sys

queue = deque()
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    command = sys.stdin.readline().rstrip().split(" ")
    if command[0] == "push":
        queue.append(command[1])
    elif command[0] == 'pop':
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if len(queue):
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if len(queue):
            print(queue[-1])
        else:
            print(-1)
