import sys
N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().rstrip().split()))
mid = round(sum(X)/len(X))
print(sum((X[i]-mid)**2 for i in range(N)))