import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = list(map(int, input().split()))

Mod = sorted(_%k for _ in A)

max_gap = 0

for i in range(n-1):
    max_gap = max(max_gap, Mod[i+1]-Mod[i])

max_gap = max(max_gap, Mod[0] + k - Mod[-1])

print(k - max_gap)