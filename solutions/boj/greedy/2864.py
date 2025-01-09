"""
숫자 5를 6으로 볼수도, 6을 5로 볼수도 있다.
"""

from sys import stdin

a, b = map(str, stdin.readline().split())

max_val = int(a.replace('5', '6')) + int(b.replace('5', '6'))
min_val = int(a.replace('6', '5')) + int(b.replace('6', '5'))

print(min_val, max_val)