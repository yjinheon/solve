# tag : greedy
# greedy에서는 문제풀이를 위한 최소한의 아이디어를 떠올리고 그게 정당한지 검토할 수 있어야 한다.

"""
3개의 시간조절용 버튼 A B C가 달린 전자레인지가 있다. 각 버튼마다 일정한 시간이 지정되어 있어 해당 버튼을 한번 누를 때마다 그 시간이 동작시간에 더해진다. 버튼 A, B, C에 지정된 시간은 각각 5분, 1분, 10초이다.

냉동음식마다 전자레인지로 요리해야할 시간 T가 초단위로 표시되어 있다. 우리는 A, B, C 3개의 버튼을 적절히 눌러서 그 시간의 합이 정확히 T초가 되도록 해야 한다.
"""
import sys

t = 391
buttons = [300, 60, 10]  # 370
cnt = [0] * 3

if (t % 10) != 0:
    print(-1)
else:
    for i in range(3):
        cnt[i] = t // buttons[i]
        t -= cnt[i] * buttons[i]
    print(cnt[0], cnt[1], cnt[2])
