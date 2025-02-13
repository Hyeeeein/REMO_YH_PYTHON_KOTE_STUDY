import sys
from collections import deque

queue = deque()
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    command = sys.stdin.readline().rstrip().split()
    if command[0] == 'push_front':
        queue.appendleft(command[1])
    elif command[0] == 'push_back':
        queue.append(command[1])
    elif command[0] == 'pop_front':
        if len(queue):
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == 'pop_back':
        if len(queue):
            print(queue.pop())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':
        if not len(queue):
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if len(queue):
            print(queue[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
