#A구 멀티탭으로 B개 플러그가 필요함
import sys
a, b = map(int, sys.stdin.readline().split())
plug = 0
count = 0
if b == 1:
    print(0)
elif a == b:
    print(1)
else:
    while plug+a < b:
        plug += a -1
        count += 1
    print(count+1)