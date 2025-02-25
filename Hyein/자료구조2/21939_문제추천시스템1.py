# recommend x = 1 ? 가장 어려운 문제, 여러 개면 문제 번호 큰 것
# recommend x = -1 ? 가장 쉬운 문제, 여러 개면 문제 번호 작은 것
# add P L 난이도 L 인 문제 번호 P 추가
# solved P 문제 P 를 제거

import sys
import heapq

N = int(sys.stdin.readline())

max_heap = []  # (난이도, 문제 번호) (최대 힙)
min_heap = []  # (난이도, 문제 번호) (최소 힙)
dict = {}  # {문제 번호: 난이도}

for _ in range(N):
    P, L = list(map(int, input().split()))
    heapq.heappush(max_heap, (-L, -P))  # 최대 힙 (난이도, 문제 번호를 음수로)
    heapq.heappush(min_heap, (L, P))   # 최소 힙
    dict[P] = L


M = int(sys.stdin.readline())


for _ in range(M):
    command = input().split()

    if command[0] == "recommend":
        if int(command[1]) == 1:
            # 어려운 문제
            while -max_heap[0][1] not in dict or dict[-max_heap[0][1]] != -max_heap[0][0]:
                heapq.heappop(max_heap)  # 삭제된 문제 제거
            print(-max_heap[0][1])  # 문제 번호 출력
        else:
            # 문제 찾기
            while min_heap[0][1] not in dict or dict[min_heap[0][1]] != min_heap[0][0]:
                heapq.heappop(min_heap)  # 삭제된 문제 제거
            print(min_heap[0][1])  # 문제 번호 출력

    elif command[0] == "add":
        P, L = int(command[1]), int(command[2])
        heapq.heappush(max_heap, (-L, -P))  # 최대 힙 추가
        heapq.heappush(min_heap, (L, P))    # 최소 힙 추가
        dict[P] = L  # 딕셔너리에 저장

    elif command[0] == "solved":
        P = int(command[1])
        if P in dict:
            del dict[P]  # 문제 삭제