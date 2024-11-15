a,b = map(int,input().split())
data =list(map(int,input().split()))

c = a * b

for i in data:
    print(i-c , end = " ")
