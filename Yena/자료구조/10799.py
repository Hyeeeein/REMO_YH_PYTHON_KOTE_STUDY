import sys

brackets = sys.stdin.readline().rstrip()

result = 0  # 잘려진 쇠막대기 조각들의 총 개수
current_pipe = 0  # 현재 겹쳐 있는 쇠막대기의 수
opened = True  # ( 이후로 아직 닫히지 않았으면 True

for ch in brackets:
    if ch == '(':
        # (를 만나면 새로운 쇠막대기 시작
        current_pipe += 1
        opened = True
    else:
        if opened:
            # 직전에 (가 있었고 바로 )가 이어진 경우 -> 레이저
            current_pipe -= 1  # 쇠막대기가 아니라 레이저였음!
            result += current_pipe  # 현재 스택에 쌓여 있는 막대기들은 모두 잘림
            opened = False
        else:
            # 이미 (가 닫힌 상태에서 )를 만난 경우 -> 쇠막대기의 끝
            current_pipe -= 1  # 막대기 하나가 끝났으므로 스택에서 제거
            result += 1  # 끝난 막대기 조각이 추가로 생김
            opened = False

print(result)
