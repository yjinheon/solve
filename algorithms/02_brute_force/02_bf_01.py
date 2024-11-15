def solve(n):
    for i in range(2, 1_000_001):
        if n % i == 0:  # 100만 이하의 divisor가 있다
            print("NO")
            break
        if i == 1_000_000:  # 100만 이하의 divisor가 없다
            print("YES")


def main():
    test_case = int(input())
    for _ in range(test_case):
        n = int(input())
        solve(n)
