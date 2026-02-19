import sys
from bisect import bisect_right
input = sys.stdin.readline

def missing(A, t):
    return t - bisect_right(A, t)

def main():
    exep_list_length, test_cases = map(int, input().split())
    exep_list = sorted(list(map(int, input().split())))
    for order in range(test_cases):
        start, added = map(int, input().split())
        base = missing(exep_list, start-1)
        target = base + added
        lo = start
        hi = start + added + exep_list_length
        while lo < hi:
            mid = (lo + hi) // 2
            if missing(exep_list, mid) >= target:
                hi = mid
            else:
                lo = mid + 1
        sys.stdout.write(str(lo)+'\n')

if __name__ == "__main__":
    main()

## Exhaustive Search was TLE so using Binary Search