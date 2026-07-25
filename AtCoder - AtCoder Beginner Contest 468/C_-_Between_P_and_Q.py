def main():
    n = int(input())
    p = tuple(map(int, input().split()))
    q = tuple(map(int, input().split()))
    from itertools import permutations
    result = 0
    for perm in permutations(range(1, n + 1)):
        if p < perm < q:
            result += 1

    print(result)



if __name__ == '__main__':
    main()