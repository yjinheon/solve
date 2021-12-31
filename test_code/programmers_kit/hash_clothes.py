import collections
import functools

"""
yellow_hat
blue_sunglasses
green_turban
yellow_hat + blue_sunglasses
green_turban + blue_sunglasses
none

3(yellow_hat,green_turban,none) * none(1)

3(yellow_hat,green_turban,none) * blue_sunglases
"""

def solution(clothes):
    answer = {}
    for i in clothes: # 배열 순회를 통해 dictionary count
        if i[1] in answer:
            answer[i[1]] += 1
        else:
            answer[i[1]] = 1
    breakpoint()
    cnt = 1
    for i in answer.values():
        cnt *= (i+1) # 각 항목수 +1  해서 곱하기
    return cnt - 1

temp = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(temp))


# 훨씬 깔끔한 방법
def solution2(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes]) # Counter 용법 참고
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer