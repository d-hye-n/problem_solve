import sys
ipnut = sys.stdin.readline

def main():
    total_length, nums_house = map(int, input().split())
    house_locate = list(map(int, input().split()))
    max_gap = 0
    for i in range(nums_house-1):
        current_gap = house_locate[i+1] - house_locate[i]
        max_gap = max(max_gap, current_gap)
    max_gap = max(max_gap, total_length-house_locate[-1]+house_locate[0])
    print(total_length-max_gap)

if __name__ == "__main__":
    main()