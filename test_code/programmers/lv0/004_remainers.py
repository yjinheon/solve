def solution(n1: int, n2: int) -> int:
    ans = n1 % n2
    print(ans)

    return ans


if __name__ == "__main__":
    n1, n2 = 3, 2
    solution(n1, n2)
