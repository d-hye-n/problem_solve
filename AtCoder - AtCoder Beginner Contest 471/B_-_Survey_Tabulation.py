def main():
    n = int(input())
    answers = []
    for i in range(n):
        answers.append(str(input()).lower())

    from collections import Counter
    print(Counter(answers).most_common(1)[0][1])

if __name__ == '__main__':
    main()