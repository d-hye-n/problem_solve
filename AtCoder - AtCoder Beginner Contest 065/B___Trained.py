import sys
N = {i+1:0 for i in range(int(sys.stdin.readline()))}
for key in N:
    value = int(sys.stdin.readline())
    N[key] = value
step = 1
count = 0
visited = set()
while step != 2:
    if step in visited:
        count = -1
        break
    visited.add(step)
    step = N[step]
    count +=1

print(count)