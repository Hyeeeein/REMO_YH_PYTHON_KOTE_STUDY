import sys

tree = {}
total = 0

for line in sys.stdin:
    t = line.rstrip("\n")
    tree[t] = tree.get(t, 0) + 1
    total += 1

for k in sorted(tree.keys()):
    percentage = tree[k] * 100.0 / total
    print(f"{k} {percentage:.4f}")
