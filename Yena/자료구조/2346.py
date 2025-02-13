import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
balloons = deque(map(int, sys.stdin.readline().rstrip().split()))
orders = deque([i+1 for i in range(N)])
popped_list = []
for _ in range(N):
    paper = balloons.popleft()
    popped_list.append(str(orders.popleft()))
    if not balloons:
        break
    if paper > 0:
        balloons.rotate(-paper+1)
        orders.rotate(-paper+1)
    else:
        balloons.rotate(-paper)
        orders.rotate(-paper)

print(" ".join(popped_list))
