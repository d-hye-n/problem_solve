import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
dest = [0] * (N+1)
for i in range(N, 0, -1):
    next_node = A[i-1]
    if next_node == i:
        dest[i] = i
    else:
        dest[i] = dest[next_node]

print(*(dest[1:]))