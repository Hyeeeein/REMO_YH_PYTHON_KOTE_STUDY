import sys
from collections import deque

# 입력 받기
input = sys.stdin.readline

N = int(input())  # 노드 개수

tree = [[] for _ in range(N+1)]  # 트리 구조 저장 (인접 리스트)
parent = [0] * (N+1)  # 부모 정보를 저장할 리스트

# 트리 입력 받기
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

# BFS 탐색 (큐 사용)
def bfs():
    queue = deque([1])  # 루트 노드는 1
    while queue:
        node = queue.popleft()  # 현재 노드
        for neighbor in tree[node]:  # 연결된 노드들 확인
            if parent[neighbor] == 0:  # 아직 부모가 없는 경우 (= 방문하지 않은 노드)
                parent[neighbor] = node  # 부모 설정
                queue.append(neighbor)  # 다음 탐색할 노드 추가

bfs()

# 부모 노드 출력 (2번 노드부터 N번 노드까지)
for i in range(2, N+1):
    print(parent[i])
