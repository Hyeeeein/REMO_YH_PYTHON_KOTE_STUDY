import sys

N = int(sys.stdin.readline().rstrip())

for i in range(N):
    strings = sys.stdin.readline().rstrip()
    count = 0
    for s in strings:
        if s == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            break
    if count == 0:
        print("YES")
    else:
        print("NO")
