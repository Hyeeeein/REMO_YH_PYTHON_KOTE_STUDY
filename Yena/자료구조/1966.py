from collections import deque
import sys

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    _, target = map(int, sys.stdin.readline().rstrip().split())
    importance_list = list(map(int, sys.stdin.readline().rstrip().split()))
    importance_queue = deque()
    idx_queue = deque()
    out_count = 0
    for im_idx, im in enumerate(importance_list):
        importance_queue.append(im)
        idx_queue.append(im_idx)
    while True:
        if importance_queue[0] < max(importance_queue):
            importance_queue.rotate(-1)
            idx_queue.rotate(-1)
        else:
            if idx_queue[0] == target:
                out_count += 1
                print(out_count)
                break
            else:
                importance_queue.popleft()
                idx_queue.popleft()
                out_count += 1