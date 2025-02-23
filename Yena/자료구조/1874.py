import sys

N = int(sys.stdin.readline().rstrip())
current = 1
stack = []
result = []

for _ in range(N):
    target = int(sys.stdin.readline().rstrip())

    while current <= target:
        stack.append(current)
        current += 1
        result.append('+')

    if stack and stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        result = "NO"
        break

# 결과 출력
if result == "NO":
    print(result)
else:
    print('\n'.join(result))

