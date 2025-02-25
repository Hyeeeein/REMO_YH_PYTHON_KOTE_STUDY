import sys, heapq

N = int(sys.stdin.readline())

max_heap = []  # 최대 힙

for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:  
        heapq.heappush(max_heap, -x) 
    else:
        if len(max_heap) == 0:
            print(0)
        else:
            maxValue = max_heap[0]
            print(-maxValue)
            heapq.heappop(max_heap)