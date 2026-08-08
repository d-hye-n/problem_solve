def main():
    n = int(input())
    lis = list(map(int, input().split()))
    import collections
    m = collections.Counter(lis).most_common(1)[0][1]
    print(n-m)

if __name__ == '__main__':
    main()