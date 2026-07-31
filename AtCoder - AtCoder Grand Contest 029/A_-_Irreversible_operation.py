def main():
    count = 0
    non_w = 0

    for c in input().strip():
        if c == "W":
            count += non_w
        else:
            non_w += 1

    print(count)


if __name__ == "__main__":
    main()