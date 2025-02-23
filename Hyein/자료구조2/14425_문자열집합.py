import sys
input = sys.stdin.readline  # 🔥 이 한 줄이 중요!

N, M = map(int, input().split())

result = 0
nameDict = {}

for i in range(N):
    name = input().strip()
    nameDict[name] = i

for i in range(M):
    problem = input().strip()
    if problem in nameDict: 
        result += 1

print(result)
