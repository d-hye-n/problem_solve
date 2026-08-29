from bisect import bisect_left


def main():
    n = int(input())
    cookies = list(map(int, input().split()))
    cookies.sort()

    now = 0
    move = 0

    r = bisect_left(cookies, now)
    l = r - 1
    for _ in range(n):
        if l < 0:
            next_val = cookies[r]
            r += 1
        elif r >= n:
            next_val = cookies[l]
            l -= 1
        else:
            l_val = cookies[l]
            r_val = cookies[r]

            l_dist = abs(l_val - now)
            r_dist = abs(r_val - now)

            if r_dist < l_dist:
                next_val = r_val
                r += 1
            else:
                next_val = l_val
                l -= 1

        move += abs(next_val - now)
        now = next_val

    print(move)


if __name__ == '__main__':
    main()
