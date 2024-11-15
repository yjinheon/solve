# tag : greedy


"""
입력:
a팀 스코어
b팀 스코어

출력 :
a 팀 승수 
무승부 수
b팀 승수
"""

from sys import stdin

a = int(stdin.readline())
b = int(stdin.readline())

# 어떤 조건에서 승점계산이 불가능해지는지 파악하는 것이 핵심
if a % 3  != b % 3:
    print(-1)
else:
    print(a//3,a%3,b//3,end=" ")
    
