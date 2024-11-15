ex = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def kthnum(array, commands):
    answer = []

    for i in commands:
        temp = array[i[0] - 1 : i[1]]
        temp = sorted(temp)
        answer.append(temp[i[2] - 1])

    return answer


def main(arr, commands):
    res = []
    for i in commands:
        tmp = arr[i[0] - 1 : i[1]]  # 전체 배열에서 1번째 index 에서 5번쩨 index 까지
        print(f"i : {i} , arr : {tmp}")
        tmp = sorted(tmp)
        print(f"arr : {tmp}")
        res.append(tmp[i[2] - 1])  # 정렬된 배열에서 3번째 index

    return res


# lambda와 map을 활용한 풀이


def solution(array, commands):
    return list(map(lambda x: sorted(array[x[0] - 1 : x[1]])[x[2] - 1], commands))


if __name__ == "__main__":
    print(main(ex, commands))
    # print(ex[1:3])
