import sys
from collections import deque

# 입력 받기
input = sys.stdin.readline

N = int(input())  # 노드 개수

tree = [[] for _ in range(N+1)]  # 트리 구조 저장 (인접 리스트)

# 트리 입력 받기
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

M = int(input())  # 노드 개수

# 트리 입력 받기
for i in range(M):
    t, k = map(int, input().split())
    if t==2 :
        print('yes')
    else:
        if len(tree[k]) > 1:
            print('yes')
        else: print('no')