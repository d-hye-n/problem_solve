def main():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    answer = nums[n//2] - nums[n//2-1]
    print(answer)

if __name__ == '__main__':
    main()