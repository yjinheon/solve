

def factorial(n):
    if n <2 :
        return 1

    return n * factorial(n -1)

def main():
    print(factorial(9))


if __name__ == "__main__":
    main()
