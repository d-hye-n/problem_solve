def main():
    a, b, c = map(int, input().split())
    count = 0

    while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
        if a == b == c:
            print(-1)
            return

        a, b, c = (
            (b + c) // 2,
            (a + c) // 2,
            (a + b) // 2,
        )
        count += 1

    print(count)


if __name__ == "__main__":
    main()