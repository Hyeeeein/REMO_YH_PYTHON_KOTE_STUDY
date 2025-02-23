import sys

input = sys.stdin.readline

dict = {}
count = 0

while True:
    tree = input().rstrip()
    if not tree:  # 빈 줄이 입력되면 종료
        break
    dict[tree] = dict.get(tree, 0) + 1  # 나무 이름 개수 증가
    count += 1  # 전체 나무 개수 증가

for key, value in sorted(dict.items()):  # 나무 이름 기준으로 정렬
    ratio = round(value / count * 100, 4) # 소수점 4자리까지 반올림
    print('%s %.4f' % (key, ratio))