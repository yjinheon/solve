import sys

def read_line_as_input():
    for line in sys.stdin:
        a, b = map(int, line.split())
        print(a + b)


if __name__ == "__main__":
    read_line_as_input()
    



