import sys
input = sys.stdin.readline

def main():
    cases = int(input())
    for i in range(cases):
        run_restaurant()

def run_restaurant():
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    rem = A[:]
    consume_ptr = 0
    discard_ptr = 0
    for i in range(N):
        need = B[i]

        while need > 0:
            while consume_ptr < N and rem[consume_ptr] == 0:
                consume_ptr += 1
            take = rem[consume_ptr] if rem[consume_ptr] < need else need
            rem[consume_ptr] -= take
            need -= take

        expire = i - D
        while discard_ptr <= expire:
            rem[discard_ptr] = 0
            discard_ptr += 1

        while consume_ptr < N and rem[consume_ptr] == 0:
            consume_ptr += 1

    print(sum(rem))

if __name__ == '__main__':
    main()