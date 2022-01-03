# tag : greedy

"""
딸기-> 초코 -> 바나나 -> 딸기
 0       1       2        0

# 순회 매칭시 나머지 연산을 활용
# 나올 수 있는 가능성의 수로 나눈 나머지

"""
n_store = int(input())
milk_store= list(map(int,input().split()))

cnt = 0

for i in range(len(milk_store)):
    if milk_store[i] == cnt % 3 :
        cnt += 1
    
print(cnt)
    


