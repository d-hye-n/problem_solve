import sys

def solve():
    input_data = sys.stdin.readline().strip()
    if not input_data:
        return
    h = int(input_data)
    if h == 0:
        print(0)
        return

    result = (1 << h.bit_length()) - 1
    print(result)

def main():
    solve()

if __name__ == "__main__":
    main()