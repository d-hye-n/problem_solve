def main():
    a, b = map(int, input().split())
    if a+b == 9:
        print("Nine")
    elif a-b == 9:
        print("Nine")
    elif a*b == 9:
        print("Nine")
    elif a/b == 9:
        print("Nine")
    else:
        print("Nein")

if __name__ == "__main__":
    main()