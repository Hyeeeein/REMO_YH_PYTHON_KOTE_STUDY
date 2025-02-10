import sys
from collections import deque


stack = []
N = int(sys.stdin.readline())


def main(commands):

    if commands[0] == 'push' :
        stack.append(int(commands[1]))
    
    elif commands[0] == 'top' :
        if len(stack) == 0 :
            print (-1)
        else :
            print(stack[-1])
    
    elif commands[0] == 'size' :
        print(len(stack))
    
    elif commands[0] == 'empty' :
        if len(stack) == 0 :
            print(1)
        else :
            print(0)
    
    elif commands[0] == 'pop' :
        if len(stack) == 0 :
            print (-1)
        else :
            popNum = stack.pop()
            print(popNum)


for _ in range(N) :
    commends = sys.stdin.readline().split()
    main(commends)