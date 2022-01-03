#data = list(map(int,input().split()))
data = [0,4,2,5,6]
data = [x**2 for x in data]
print(sum(data) % 10)
