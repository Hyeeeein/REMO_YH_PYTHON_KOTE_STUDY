import sys, heapq

N = int(sys.stdin.readline())
array = list(map(int, input().split()))
stack = []

for num in array:
	heapq.heappush(stack, num) #

for line in range(N - 1):
    newArray = list(map(int, input().split()))

    for num in newArray:
        if stack[0] < num: # q 최솟값보다 현재 숫자가 클 경우 n번째로 큰 수가 바뀌어야 하기 때문에
            heapq.heappush(stack, num) # 현재 숫자를 push 하고
            heapq.heappop(stack) # 기존 최솟값 pop


print(stack[0])