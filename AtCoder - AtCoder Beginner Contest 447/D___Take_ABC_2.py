S = input().strip()

a = 0
ab = 0
ans = 0

for char in S:
    if char == 'A':
        a += 1
    elif char == 'B':
        if a > 0:
            a -= 1
            ab += 1
    else:
        if ab > 0:
            ab -= 1
            ans += 1

print(ans)