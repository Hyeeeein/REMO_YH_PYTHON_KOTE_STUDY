from collections import deque

N,K = map(int,input().split())

circle = deque([i for i in range(1, N+1)])

def main():
    removed_list = []
    while circle:
        circle.rotate(-K)
        removed_list.append(str(circle.pop()))
    print("<" + ", ".join(removed_list) + ">")


main()