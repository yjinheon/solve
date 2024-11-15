"""
 삽입 정렬
    -  손안 의 카드를 정렬하는 방법과 유사
    -  정렬되지 않은 숫자를 이미 정렬된 부분의 적절한 위치에 삽입하는 방식
    - 시간 복잡도: O(n^2)
    - 공간 복잡도: O(n)
    - 자료배열의 모든요소를 앞에서부터 차례대로 이미 정렬된 배열부분과 비교하여 자신의자리를 찾아 삽입
"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1  # to keep track of the sorted part of the array
    return arr


test_arr = [5, 2, 1, 4, 3]

insertion_sort(test_arr)

if __name__ == "__main__":
    print(insertion_sort(test_arr))
