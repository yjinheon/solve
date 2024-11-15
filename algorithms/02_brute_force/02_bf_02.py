test_case = int(input())


def solve(n):
    for i in range(2, 1_000_001):
        if n % i == 0:  # 100만 이하의 divisor가 있다
            print("NO")
            break
        if i == 1_000_000:  # 100만 이하의 divisor가 없다
            print("YES")


def solve2():
    candy = 6

    res = 0

    for A in range(0, candy + 1):
        for B in range(0, candy + 1):
            for C in range(0, candy + 1):
                if A + B + C == candy:
                    if A >= B + 2:
                        if A != 0 and B != 0 and C != 0:
                            if C % 2 == 0:
                                res += 1

    return res


def solve3():
    a, b, c, d, e, f = map(int, (input().split()))
    pass


def main():
    for _ in range(test_case):
        n = int(input())
        solve(n)
