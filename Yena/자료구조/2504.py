import sys

string = sys.stdin.readline().rstrip()
stack = []
calc_stack = []

current = None
for idx, s in enumerate(string):
    if s == "(":
        stack.append(s)
        calc_stack.append([s, 2])
    elif s == "[":
        stack.append(s)
        calc_stack.append([s, 3])
    else:
        if not len(stack):
            print(0)
            exit(0)
        if s == ")" and not (stack[-1] == "("):
            print(0)
            exit(0)
        elif s == "]" and not (stack[-1] == "["):
            print(0)
            exit(0)
        else:
            stack.pop()
            cur_s, cur_n = calc_stack.pop()
            if cur_s is None:
                prev_s, prev_n = calc_stack.pop()
                calc_stack.append([None, prev_n * cur_n])
            else:
                calc_stack.append([None, cur_n])
            while len(calc_stack) >= 2:
                s1, n1 = calc_stack[-1]
                s2, n2 = calc_stack[-2]
                if s1 or s2:
                    break
                calc_stack.pop()
                calc_stack.pop()
                calc_stack.append([None, n1 + n2])

if len(stack):
    print(0)
    exit(0)

print(calc_stack[-1][1])

