# sys.stdin.readline 을 사용한 입력

from sys import stdin

data = int(stdin.readline()) : 한개의 정수를 입력받을 경우

## 한개의 정수 입력받기
import sys
a = int(sys.stdin.readline())

## 정해진 개수의 정수를 한줄에 입력받기
"""

보통 개수가 3~5개정도로 적을 경우 사용

"""

import sys
a,b,c,d,e = map(int,sys.stdin.readline().split())

## 임의의 개수의 정수를 한줄에 입력 받고 리스트로 저장

import sys
l = list(map(int,sys.stdin.readline().split()))

## 임의의 개수의 정수를 n줄 입력받아 2차원리스트에 저장
import sys
l = [] # 초기화
n = int(sys.stdin.readline())

for i in range(n):
    l.append(list(map(int,sys.stdin.readLine().split())))


## 문자열 n줄을 입력받아 리스트에 저장

import sys
n = int(sys.stdin.readLine())
l = [sys.stdin.readline().strip() for i in range(n)]

# 데이터의 개수 입력

n = int(input())

# 공백 구분자로 입력

data = list(map(int, input().split()))

# 문자열 입력받기

import sys

data = sys.stdin.readline().rstrip
print(data)
