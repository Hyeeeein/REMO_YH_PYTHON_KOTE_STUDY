import sys
from collections import deque

N, K = map(int, sys.stdin.readline().rstrip().split(" "))
circle = deque([i+1 for i in range(N)])
removed_list = []

while len(circle):
    circle.rotate(-K)
    print(circle)
    removed_list.append(str(circle.pop()))
    print(removed_list)

out_str = "<"
out_str += ", ".join(removed_list)
out_str += ">"
print(out_str)
