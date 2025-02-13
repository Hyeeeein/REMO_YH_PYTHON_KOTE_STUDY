import sys
from collections import deque


N = int(sys.stdin.readline())
card = list(sys.stdin.readline().strip().split(' '))
balloons = deque([[i+1, int(card[i])] for i in range(N)]) 

result = []

while balloons:
    num, paper = balloons.popleft()
    result.append(str(num))

    if paper > 0 :
        balloons.rotate(-(paper - 1))
    else :
        balloons.rotate(-paper)

print(' '.join(result))

