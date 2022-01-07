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

if a % 3  != b % 3:
    print(-1)
else:
    print(a//3,a%3,b//3,end=" ")
    