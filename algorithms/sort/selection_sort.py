test_arr = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

"""
선택정렬
- 기본적으로 가장 작은 걸 선택해서 앞으로 보낸다.
"""


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


if __name__ == "__main__":
    print(selection_sort(test_arr))
