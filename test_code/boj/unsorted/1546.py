from sys import stdin

n =  int(stdin.readline())

# get n numbers

data = list(map(int, stdin.readline().split()))

# get max from data

m = max(data)

data = [(x/m) * 100 for x in data]

print(sum(data) / n)