

"""
bin() : 2진수
oct() : 8진수
hex() : 16진수

int() : 문자열을 받아서 10진수로 변환
ord() : 문자열을 받아서 문자에 해당하는 유니코드 정수 반환
chr() : 정수를 받아수 유니코드 문자열 반환
"""
import sys
s = sys.stdin.readline()
print(int(s,16))

