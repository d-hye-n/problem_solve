def solve():
    n = int(input())
    l = list(map(int, input().split()))
    nums = {}
    for i in range(n):
        nums[l[i]] = nums.get(l[i], 0) + 1
    sums = 0
    for k in nums:
        if nums[k] % 2 == 1:
            sums += k

    print(sums)
if __name__ == '__main__':
    solve()