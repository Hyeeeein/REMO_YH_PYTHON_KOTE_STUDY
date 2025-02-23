import sys

N = int(sys.stdin.readline())  

stack = [] 
result = []
find = True

now = 1

for _ in range(N):
   num = int(input())
   # 쌓기 
   while now <= num:
      stack.append(now)
      result.append('+')
      now += 1
   # 빼기
   if stack[-1] == num:
      stack.pop()
      result.append('-')
    # 불가능
   else:
      find = False

# 정답 출력
if not find: # 불가능하다면
    print('NO')
else:
    for i in result: # 가능하다면
        print(i)