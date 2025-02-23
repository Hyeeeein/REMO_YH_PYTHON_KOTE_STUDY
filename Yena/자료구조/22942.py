import sys

N = int(sys.stdin.readline().rstrip().strip())
circles = []

for _ in range(N):
    x, r = map(int, sys.stdin.readline().rstrip().split())
    begin = x - r
    end = x + r
    circles.append([begin, end])

circles.sort(key=lambda c: (c[0], c[1]))

data_check = True
end_list = []

for begin, end in circles:
    while end_list and end_list[-1] < begin:
        end_list.pop()

    if end_list and begin <= end_list[-1] <= end:
        data_check = False
        break

    end_list.append(end)

if data_check:
    print("YES")
else:
    print("NO")
