n = int(input())

hint = [list(map(int, input().split())) for _ in range(4)]


def solve():
    answer = 0
    for a in range(1, 10):  # 100의 자리수
        for b in range(10):  # 10의자리수
            for c in range(10):  # 1의 자리수
                if a == b or b == c or c == a:
                    continue
                # 숫자가 정해짐
                cnt = 0
                for arr in hint:
                    num = hint[0]
                    ball = hint[1]
                    strike = hint[2]

                    # a,b,c 를 number와 비교
                    # 자리수를 나눠서 strike ball 측정
                    # 100의 자리 가 같을 경우

                    # abc가 정답의 숫자 포함되어 있다면 ball count 증가
                    str_num = str(num)
                    # 정답과 자릿수가 일치할 경우 strike count 증가
                    for x in str_num:
                        ball_count = 0
                        strike_count = 0
                        for i in range(3):
                            if str_num[i] == x:
                                strike_count += 1
                            elif x in str(a) + str(b) + str(c):
                                ball_count += 1

                        if ball == ball_count and strike == strike_count:
                            cnt += 1

                if cnt == n:
                    answer += 1
                    print(answer)


def main():
    A, B, C, D, E, F = map(int, input().split())
