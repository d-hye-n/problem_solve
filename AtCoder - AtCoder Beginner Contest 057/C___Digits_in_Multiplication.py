import math

def split_by_product(N):
    r = int(math.isqrt(N))
    for a in range(r, 0, -1):
        if N % a == 0:
            return a, N // a

def main():
    N = int(input())
    A, B = split_by_product(N)
    print(len(str(max(A,B))))

if __name__ == '__main__':
    main()