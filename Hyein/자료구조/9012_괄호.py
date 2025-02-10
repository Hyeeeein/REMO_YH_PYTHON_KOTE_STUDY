import sys

N = int(sys.stdin.readline())

def main(line: str):
    stack = []
    for i in list(line):
        if i == '(':
            stack.append(i)
        elif i == ')':
            if stack:
                stack.pop()
            else: # 괄호 X => NO 출력하고 끝
                print("NO")
                break
    else: # 앞서 break 로 끝나지 않았을 경우
        if not stack: 
            print("YES")
        else: # 스택에 괄호 남아있다면 NO 출력
            print("NO")

for i in range(N) :
    line = sys.stdin.readline().split()[0]
    main(line)