import sys
import heapq

N = int(sys.stdin.readline().rstrip())
heap = []
for i in range(N):
    x = int(sys.stdin.readline().rstrip())
    if x == 0:
        if heap:
            print(-heapq.heappop(heap))
        else:
            print(0)
    heapq.heappush(heap, -x)
