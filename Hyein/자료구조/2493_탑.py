import sys
from collections import deque

N = int(sys.stdin.readline())  
towerList = list(map(int, sys.stdin.readline().split())) 

stack = deque()  
result = [] 


#  스택에 뒤로 갈수록 가까운 낮은 탑은 버리고, 높을 가능성이 있는 탑은 저장해두는 방식
for i in range(N):
    while stack and stack[-1][1] < towerList[i]:  # 스택의 마지막 요소보다 현재 탑이 더 크면
        stack.pop()  # 현재 탑이 이전 탑보다 크므로 pop (이전 탑은 수신할 수 없음)

    if stack:  # 스택에 남아있는 탑이 있다면, 신호를 수신할 수 있음
        result.append(stack[-1][0] + 1)  # 인덱스는 1-based (1부터 시작)
    else:
        result.append(0)  # 수신할 탑이 없으면 0

    stack.append((i, towerList[i]))  # 현재 탑을 스택에 추가

print(" ".join(map(str, result)))  # 정답 출력


