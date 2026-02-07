import sys
n, a, b = map(int, sys.stdin.readline().split())
s = list(sys.stdin.readline())
total = a+b
b_count = 0
count = 0
for i in range(n):
    if s[i] == 'a' and count+1 <= total:
        print("Yes")
        count += 1
    elif s[i] == 'b' and count+1 <= total and b_count+1 <= b:
        print("Yes")
        b_count += 1
        count += 1
    else:
        print("No")