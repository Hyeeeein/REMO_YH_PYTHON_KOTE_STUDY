from collections import deque

nums = [1, 2, 3, 4, 5, 6]

queue = deque(nums)

queue.rotate(-3)  # 왼쪽으로 1회 회전하기
print(queue)  # deque([2, 3, 4, 5, 6, 1])

nums = [1, 2, 3, 4, 5, 6]

queue = deque(nums)

queue.rotate(3)  # 오른쪽으로 1회 회전하기
print(queue)  # deque([6, 1, 2, 3, 4, 5])
