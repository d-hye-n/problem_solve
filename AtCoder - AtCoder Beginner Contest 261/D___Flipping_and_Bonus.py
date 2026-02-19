import sys
input = sys.stdin.readline

def main():
    bet_count, bonus_count = map(int, input().split())
    bets = list(map(int, input().split()))
    bonus_list = [0]*(bet_count+1)
    for i in range(bonus_count):
        streak, bonus = map(int, input().split())
        bonus_list[streak] = bonus
    big_neg = -10**18
    dp = [big_neg] * (bet_count+1)
    dp[0] = 0

    for i in range(bet_count):
        ndp = [big_neg] * (bet_count+1)
        best = max(dp)
        ndp[0] = best
        betsi = bets[i]
        for j in range(bet_count):
            v = dp[j]
            if v == big_neg:
                continue
            nv = v + betsi + bonus_list[j+1]
            if nv > ndp[j+1]:
                ndp[j+1] = nv
        dp = ndp
    print(max(dp))


if __name__ == "__main__":
    main()