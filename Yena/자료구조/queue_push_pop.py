import sys
from collections import deque

# 입력
inp = sys.stdin.readline().rstrip().split(" ")
print(inp)

queue = deque()

# 오른쪽에 삽입
queue.append(3)
queue.append([3, 4, 5])
queue.append(10)
queue.append(100)
print(queue)

# 왼쪽에 삽입
queue.appendleft(90)
print(queue)

# 왼쪽 제거
queue.popleft()
print(queue)

# 오른쪽 제거
a = queue.pop()
print(a, queue)

