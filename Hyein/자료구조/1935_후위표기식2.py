n = int(input())

s = input()
arr_dict = {}
for i in range(n) :
    arr_dict[chr(65+i)] = int(input())

stack = []

for c in s :
    if c == '+' or c == '-' or c == '*' or c == '/' :
        n1 = stack.pop()
        n2 = stack.pop()
        if c == '+' :
            stack.append(n2 + n1)
        elif c == '-' :
            stack.append(n2 - n1)
        elif c == '*' :
            stack.append(n2 * n1)
        elif c == '/' :
            stack.append(n2 / n1)
    else:
        stack.append(arr_dict[c])
        
print('{:.2f}'.format(stack[0]))