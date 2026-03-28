import sys
import heapq
input = sys.stdin.readline

q = int(input())
tree = []
for _ in range(q):
    a, b = map(int, input().split())
    if a == 1:
        heapq.heappush(tree, b)
    elif a == 2:
        while tree and tree[0] <= b:
            heapq.heappop(tree)

    print(len(tree))