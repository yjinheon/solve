from sys import stdin

#n = int(stdin.readline().strip())

n = 5

for i in range(1,n+1):
    print(" " * (n-i) + "*" * i)
    
