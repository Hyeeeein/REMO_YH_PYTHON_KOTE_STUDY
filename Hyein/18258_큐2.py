import sys
from collections import deque


queue = deque()
N = int(sys.stdin.readline())


def main(commands):

    if commands[0] == 'push' :
        queue.append(int(commands[1]))
    
    elif commands[0] == 'pop' :
        if not queue :
            print (-1)
        else :
            print(queue[0])
            queue.popleft()
    
    elif commands[0] == 'size' :
        print(len(queue))
    
    elif commands[0] == 'empty' :
        if len(queue) == 0 :
            print(1)
        else :
            print(0)
    
    elif commands[0] == 'front' :
        if not queue:
            print(-1)
        else :
            print(queue[0])
    
    elif commands[0] == 'back' :
        if not queue :
            print(-1)
        else :
            print(queue[-1])    


for _ in range(N) :
    commends = sys.stdin.readline().split()
    main(commends)