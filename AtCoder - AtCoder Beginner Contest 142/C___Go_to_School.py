def main():
    N = int(input())
    school = list(map(int, input().split()))
    match = {school[i]:i+1 for i in range(N)}
    values = [match[k] for k in sorted(match)]
    print(*values,sep=' ')

if __name__ == '__main__':
    main()
