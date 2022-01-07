import sys

data = list(map(int,sys.stdin.readline().split()))

pieces = [1,1,2,2,2,8] # 킹,퀸,룩,비숍,나이트,폰

for i in range(len(data)):
    print(pieces[i]-data[i],end=" ")
