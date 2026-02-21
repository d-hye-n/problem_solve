def main():
    N = int(input())
    count = 0
    if N % 2 == 1:
        print(0)
        exit()
    m = N//2
    for i in range(1,28):
        count += m//5**i
    print(count)

if __name__ == '__main__':
    main()