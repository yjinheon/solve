# tag : greedy
import random

"""
거스름돈의 액수가 주어지면 리암이 줘야할 쿼터(Quarter, $0.25)의 개수, 다임(Dime, $0.10)의 개수, 니켈(Nickel, $0.05)의 개수, 페니(Penny, $0.01)의 개수를 구하는 프로그램을 작성하시오. 거스름돈은 항상 $5.00 이하이고, 손님이 받는 동전의 개수를 최소로 하려고 한다. 예를 들어, $1.24를 거슬러 주어야 한다면, 손님은 4쿼터, 2다임, 0니켈, 4페니를 받게 된다.
"""


def change(c):
    changes = [0, 0, 0, 0]
    coins = [25, 10, 5, 1]

    for _ in range(len(coins)):
        changes[_] = c // coins[_]
        c = c % coins[_]

    print(changes[0], changes[1], changes[2], changes[3])


def main():
    c = int(100 * float(random.random() * 5))
    print(c)
    change(c)


if __name__ == "__main__":
    main()

