def main():
    from functools import reduce
    import operator
    import numpy as np

    n, q = map(int, input().split())
    As = [0]*n
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            As[query[1]-1] += 1
        else:
            arr = np.array(As)
            arr[arr >= 1] -= 1
            As = arr.tolist()
        result = reduce(operator.xor, As, 0)
        print(result)

if __name__ == '__main__':
    main()

    ### TLE