import sys
input = sys.stdin.readline

def main():
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    nums_reverse = list(reversed(nums))
    right_sum, left_sum = 0, 0
    for i in range(N):
        for j in range(i):
            if nums[j] < nums[i]:
                left_sum += 1
        for j in range(i):
            if nums_reverse[j] < nums_reverse[i]:
                right_sum += 1
    result = (right_sum * K*(K+1)//2 + left_sum * (K-1)*K//2)%(10**9+7)
    print(int(result))

if __name__ == '__main__':
    main()