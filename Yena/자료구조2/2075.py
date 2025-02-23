import sys
import heapq

N = int(sys.stdin.readline().rstrip())
heap = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().rstrip().split()))
    for x in row:
        heapq.heappush(heap, x)
        if len(heap) > N:
            heapq.heappop(heap)

print(heap[0])
