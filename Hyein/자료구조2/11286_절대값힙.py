import sys, heapq

N = int(sys.stdin.readline())

min_heap = []  # 최소 힙

for _ in range(N):
    x = int(sys.stdin.readline())
    if x != 0:  
        heapq.heappush(min_heap, (abs(x), x)) 
    else:
        if len(min_heap) == 0:
            print(0)
        else:
            minValue = min_heap[0]
            print(minValue[1])
            heapq.heappop(min_heap)