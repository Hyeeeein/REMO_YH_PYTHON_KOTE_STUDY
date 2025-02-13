import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
queue = deque([i+1 for i in range(N)])

while True:
    _1 = queue.popleft()
    if not len(queue):
        print(_1)
        break
    queue.rotate(-1)

