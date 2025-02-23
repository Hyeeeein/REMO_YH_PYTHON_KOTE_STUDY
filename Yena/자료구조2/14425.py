import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
count = 0
S = []
for _ in range(N):
    s = sys.stdin.readline().rstrip()
    S.append(s)
for _ in range(M):
    t = sys.stdin.readline().rstrip()
    if t in S:
        count += 1
print(count)
