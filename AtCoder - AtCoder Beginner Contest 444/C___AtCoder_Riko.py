import sys
input = sys.stdin.readline

n = int(input())
a = sorted(list(map(int, input().split())))
#그대로 이거나 무조건 두개로 부러지거나.
#그니까 제일 큰게 원래 가장 큰 것 or 제일 큰게 가장 큰 것의 조각
def check(L):
    i, j = 0, len(a)-1
    while i <= j:
        if a[j] == L:
            j-= 1
        elif i < j and a[i] + a[j] == L:
            i += 1
            j -= 1
        else:
            return False
    return True
#ans 후보를 선정
ans = set()
ans.add(a[-1])
ans.add(a[0]+a[-1])
#ans 후보를 check에 넣어서 가능한지 판정
ans2 = []
for k in sorted(list(ans)):
    if check(k):
        ans2.append(k)
print(*ans2)