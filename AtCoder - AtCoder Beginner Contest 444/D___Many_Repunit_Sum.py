import sys
input = sys.stdin.readline
sys.set_int_max_str_digits(300000)
n = int(input())
a = list(map(int, input().split()))
#숫자계산하면 너무 오래걸림 -> 걍 리스트로 각 자라수 나타내서 1씩 올려서 합쳐
count = [0] * (max(a) + 2)
ans = []
for i in a:
    count[1] += 1
    count[i + 1] -= 1
ones = 0
for k in range(1, max(a)+1):
    ones += count[k]
    count[k] = ones
up = 0
for l in range(1, max(a)+1):
    total = count[l] + up
    ans.append(str(total % 10))
    up = total // 10
while up > 0:
    ans.append(str(up % 10))
    up //= 10

print("".join(ans[::-1]))