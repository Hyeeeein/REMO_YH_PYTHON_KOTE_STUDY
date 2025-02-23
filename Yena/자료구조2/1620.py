import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
pokemon2seq = {}
seq2pokemon = {}

for i in range(1, N+1):
    s = sys.stdin.readline().rstrip()
    idx = str(i)
    pokemon2seq[s] = idx
    seq2pokemon[idx] = s

for _ in range(M):
    s = input().strip()
    if s[0].isdigit():
        print(seq2pokemon[s])
    else:
        print(pokemon2seq[s])
