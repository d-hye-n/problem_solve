n, l, r = map(int, input().split())
s = input().strip()

pos = [[] for _ in range(26)]
for i in range(n):
    pos[ord(s[i]) - 97].append(i)

count = 0

for arr in pos:
    m = len(arr)
    left = 0
    right = 0

    for i in range(m):
        if left < i + 1:
            left = i + 1
        while left < m and arr[left] - arr[i] < l:
            left += 1

        if right < left:
            right = left
        while right < m and arr[right] - arr[i] <= r:
            right += 1

        count += right - left

print(count)