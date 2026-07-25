def main():
    num = int(input())
    list1 = list(map(int, input().split()))
    result = 0
    for i in range(1,num-1):
        a = list1[i-1]
        b = list1[i]
        c = list1[i+1]
        if a < b and b > c:
            result += 1
    print(result)

if __name__ == "__main__":
    main()