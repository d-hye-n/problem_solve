def solve():
    n, k  = map(int, input().split())
    l = list(map(int, input().split()))
    nums = {}
    ans = 0
    for i in range(n):
        nums[l[i]] = nums.get(l[i], 0) + 1

    max_num = max(nums.values())

    for k in nums:
        if max(nums[k]+1,max_num) == nums[k]+1:
            ans += 1

    print(ans)

if __name__ == '__main__':
    solve()