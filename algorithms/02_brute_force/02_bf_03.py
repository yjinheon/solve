def solve(A, B, C, D, E, F):
    for x in (-10000, 10001):
        for y in (-10000, 10001):
            if A * x + B * y == C:
                if D * x + E * y == F:
                    print(x, y)
                    break


def main():
    A, B, C, D, E, F = map(int, input().split())
