# 구구단 
from sys import stdin

n = int(stdin.readline().strip())

for i in range(1, 10):
    print(n, '*', i, '=', n * i)