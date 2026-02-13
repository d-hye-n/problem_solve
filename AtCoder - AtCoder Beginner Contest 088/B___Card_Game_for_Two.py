N = int(input())
nums = sorted(list(map(int, input().split())), reverse=True)

result = sum(nums[0::2]) - sum(nums[1::2])
print(result)