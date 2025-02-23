import sys

N = int(sys.stdin.readline())  

for _ in range(N):
    n, m = map(int, input().split())
    papers = list(map(int, input().split()))
    result = 1
    while papers :
        if papers[0] < max(papers): # 현재 문서가 다른 문서들의 중요도보다 낮다면
            papers.append(papers.pop(0)) # 빼서 뒤로 보내기
        else :
            if m == 0: # 추적 문서가 0?
                break

            papers.pop(0)
            result += 1

        if m > 0: # 큐의 맨뒤로, 현재 문서 프린트?
            m = m - 1  # 추적문서 1 감소
        else: # 중요도 높은 문서 있나? 
            m = len(papers) - 1  # 남은 문서양의 - 1

    print(result)