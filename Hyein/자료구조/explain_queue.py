# 큐 설명 - 예나님

import sys
from collections import deque

queue = deque()
inp = sys.stdin.readline().rstrip().split(" ") # 이렇게 해야 빠르다고 함(js 랑 비슷한듯?)
print(inp)

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