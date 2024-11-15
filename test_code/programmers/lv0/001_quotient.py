# n1, n2 = map(int, input().split())


def solve(n1: int, n2: int) -> int:
    solution = 0

    solution = n1 // n2
    print(solution)

    return solution


if __name__ == "__main__":
    n1, n2 = 10, 5
    solve(n1, n2)
