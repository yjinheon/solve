# tag : greedy

"""
캥거루 세 마리가 사막에서 놀고 있다. 사막에는 수직선이 하나 있고, 캥거루는 서로 다른 한 좌표 위에 있다.

한 번 움직일 때, 바깥쪽의 두 캥거루 중 한 마리가 다른 두 캥거루 사이의 정수 좌표로 점프한다. 한 좌표 위에 있는 캥거루가 두 마리 이상일 수는 없다.

캥거루는 최대 몇 번 움직일 수 있을까?


"""

# 최대로 움직일려면 gap이 가장 긴 지점에서 최소 거리로 이동하몀 된다.
# 테스트 케이스가 여려개 있을 경우 while문과 try except문을 사용한다.

temp = [3,5,9]

#temp = [1,5,6]


# solution 1        

while True:
    try:
        cnt = 0
        temp = list(map(int, input().split()))
        gap1 = temp[1] - temp[0]
        gap2 = temp[2] - temp[1]
        if gap1 == 1 and gap2 == 1:
            break
        elif gap1 < gap2 :
            temp[0] = temp[1]
            temp[1] = temp[1] + 1
            cnt +=1
        else :
            temp[2] = temp[1]
            temp[1] = temp[0] +1
            cnt += 1
        print(cnt)
    except:
        break

# solution 2

while True:
    try:
        A, B, C = map(int, input().split())
        print(max(B-A, C-B)-1)
    except:
        break
