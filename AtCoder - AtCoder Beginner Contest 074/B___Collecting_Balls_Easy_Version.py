def main():
    N = int(input())
    K = int(input())
    cords = list(map(int, input().split()))
    result = 0
    for i in cords:
        result += 2*min(i, K-i)
    print(result)

if __name__ == "__main__":
    main()