import sys
import string

N = int(sys.stdin.readline().rstrip())
equation = sys.stdin.readline().rstrip()
operator = '+-*/'
alp2num = {}
stack = []

for alp_idx, alp in enumerate(string.ascii_uppercase):
    alp2num[alp] = int(sys.stdin.readline().rstrip())
    if alp_idx == N-1:
        break

for eq in equation:
    if eq not in operator:
        stack.append(alp2num[eq])
    else:
        if eq == '+':
            _1 = stack.pop()
            _2 = stack.pop()
            stack.append(_1+_2)
        elif eq == '-':
            _1 = stack.pop()
            _2 = stack.pop()
            stack.append(_2-_1)
        elif eq == '*':
            _1 = stack.pop()
            _2 = stack.pop()
            stack.append(_1*_2)
        else:
            _1 = stack.pop()
            _2 = stack.pop()
            stack.append(_2/_1)

print(f"{stack[0]:.2f}")
