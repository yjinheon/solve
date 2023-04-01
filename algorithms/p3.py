'''
요구사항:
Part 2에 이어 추가적인 상황을 해결해보자.

중요한 조건은 아래 주어진 코드처럼 재귀를 반드시 활용해야 합니다.

2개의 숫자(양수와 음수 모두 가능)가 입력되었을 경우, 처리해주는 코드를 추가로 작성하세요.

입력받은 문자가 양수인지 음수인지 판별을 먼저 진행해야 합니다.

입출력의 형태는 리스트, 딕셔너리 등 다양하게 활용하셔도 됩니다.
'''
# 아래 counter 클래스는 변경하지 마세요!
class counter:
    def __init__(self, function):
        self.function = function
        self.cnt = 0

    def __call__(self, *args, **kwargs):
        self.cnt += 1
        return self.function(*args, **kwargs)


@counter    # 삭제하지 마세요!
def print_to_zero_pos_neg(nums, dir):
    if type(nums)==str:
        for i in nums.split(','):
            templist=print_to_zero_pos_neg(int(i),[])
            dir[i]=templist
        return dir
    elif type(nums)==int:
        dir.append(str(nums))
        if nums==0:
            return dir
        elif nums>0:
            return print_to_zero_pos_neg(nums-1,dir)
        else:
            return print_to_zero_pos_neg(nums+1, dir)


if __name__ == "__main__":
    res = {}
    print_to_zero_pos_neg('-10,10,5,-5', res)
    import pprint
    pprint.pprint(res)

