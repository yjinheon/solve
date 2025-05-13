#y = int(input())
y = 2000


def solve(year):

    cond1 = year % 4 == 0
    cond2 = year % 400 == 0
    cond3 = year % 100 != 0

    if cond1:
        if cond2:
            print(1)
        elif cond3:
            print(1)
        else:
            print(2)
    else:
        print(2)


if __name__ == "__main__":
    solve(y)
