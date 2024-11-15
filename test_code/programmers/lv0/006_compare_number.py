def solution(n1: int, n2: int) -> int:
    answer = 0

    if n1 == n2:
        answer = 1
    else:
        answer = -1

    return answer


if __name__ == "__main__":
    n1, n2 = 10, 5
    solution(n1, n2)
