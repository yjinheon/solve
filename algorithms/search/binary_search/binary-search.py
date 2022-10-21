"""
- 시간복잡도가 Log2N
- 자료의 크기가 클수록 선형탐색에 비해 성능이 우수해짐
- 자료가 정렬되어 있다는 전제가 필요

ref
- https://soooprmx.com/
- https://www.geeksforgeeks.org/python-program-for-binary-search/

"""
from random import randint
import time


# decorator 를 활용한 실행시간 측정
def check_time(func):
    def wrapper_fn(*args,**kwargs):
        start_time = time.time()
        func_result = func(*args,**kwargs)
        print(f"Processing time is {(time.time()-start_time):.2f}")
        return func_result
    return wrapper_fn

@check_time
def bin_search(arr,target):
    left, right = 0, len(arr) # 리스트의 전체구역을 대상으로함

    while True:
        if left == right:
            return -1 # 구간의 길이가 0 이면 답없음
        mid = (left+right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            left, right = left , mid

        else: # 구간을 오른쪽 절반으로 줄임
            left, right = mid+1 ,right



# 재귀를 활용한 이진 탐색

@check_time
def binary_search_iter(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search_iter(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search_iter(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1


temp_arr = [randint(100,1000000) for _ in range(1000000)]
ys = sorted(temp_arr)

k = ys[87]
k2 = randint(100,1000000)


if __name__ == "__main__":
    a=bin_search(temp_arr,k)
    print(a)
    print(f"k is {k}")
    print(f"k2 is {k2}")
    res = binary_search_iter(temp_arr,100,1000000,k2)
    if res != -1:
        print("Element is present at index", str(res))
    else:
        print("Element is not present in array")
    print("Done")


