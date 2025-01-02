n = int(input())


def factorial(n):
    res = 1

    for i in range(1, n + 1):
        res *= i

    return res


def main():
    print(factorial(n))


if __name__ == "__main__":
    main()
