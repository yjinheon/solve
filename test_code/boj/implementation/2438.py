from sys import stdin

n_star = int(stdin.readline().strip())


for i in range(1,n_star+1):
    print("*" * i, end="\n")
