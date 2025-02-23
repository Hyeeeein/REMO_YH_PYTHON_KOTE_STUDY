import sys
input = sys.stdin.readline  # 🔥 이 한 줄이 중요!

N, M = map(int, input().split())

nameDict = {}
numDict = {}

for i in range(N):
    name = input().strip()
    nameDict[name] = i + 1
    numDict[i + 1] = name

for i in range(M):
    problem = input().strip()
    if problem.isdigit():
        print(numDict[int(problem)])
    else:
        print(nameDict[problem])
