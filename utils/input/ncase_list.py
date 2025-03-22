"""
첫째줄 n_test_case를 입력받고, 

n_test_case만큼 a, b를 입력받아 a, b 에 대한 어떤 처리를 하는 패턴

"""

def print_case():
    n_case = int(input())

    for _ in range(n_case):
        a, b = map(int, input().split())
        print(f"a = {a}, b = {b}")


if __name__ == "__main__":
    print_case()
