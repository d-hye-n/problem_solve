def main():
    m, d = map(int, input().split())
    list1 = list(input())
    result = [c == '.' for c in list1]
    for k in range(m):
        if list1[k] == 'G':
            start = max(0, k - d)
            end = min(m, k + d + 1)
            for i in range(start, end):
                result[i] = False
    print(result.count(True))



if __name__ == "__main__":
    main()