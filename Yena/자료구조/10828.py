import sys

stack = []
N = int(sys.stdin.readline().rstrip())
for i in range(N):
    command = sys.stdin.readline().rstrip().split(" ")
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == 'pop':
        if len(stack):
            print(stack.pop(-1))
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)

