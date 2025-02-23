import sys

pList = list(sys.stdin.readline())

stack = []
result = 0

for i in range(len(pList)):
    # ( 가 나오면 스택에 넣기
    if pList[i] == "(": 
        stack.append("(")
    
    # ) 가 나올 경우
    else : 
        if pList[i-1] == "(": # 그다음이 (일 때 
            stack.pop()
            result += len(stack) # 첫 번째 경우인 현재의 쇠막대기들을 카운팅합니다.
            
        else :
            stack.pop()
            result += 1 # 이 부분은 두 번째 경우인 나머지 부분을 세는 것입니다.


print(result)