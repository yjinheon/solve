"""
- 기본적으로 1개의 서브리스트가 나올때까지 분할을 진행
- 이후 배열값을 반복문을 통해 비교 -> 정렬 ->교환 후 합치기

ref : https://www.geeksforgeeks.org/merge-sort/

"""

def merge_sort(arr):
    if len(arr) >1 :
        mid = len(arr) // 2 # 배열의 중간 찾기

        left = arr[:mid] # 나눠진 왼쪽부분
        right = arr[mid:] # 나눠진 오른쪽 부분

        # 재귀 분할정복
        merge_sort(left) # 왼쪽부분에 대해 정렬 함수 호출을 통해 정렬
        merge_sort(right) # 오른쪽 부분에 대해 정렬함수 호출을 통해 정렬

        i = j = k = 0

        # 배열의 인덱스를 참조하여 비교-> 정렬 -> 교환

        while i <len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i] # 왼쪽 값을 결과를 위한 값에 저장 
                i += 1  # 왼쪽 배열값 인덱스 1 증가

            else: # 왼쪼값  > 오른쪽 값
                arr[k] = right[j]
                j += 1

            k +=1

        #왼쪽과 오른쪽에 대해 중간정렬 결과 확인
        print(left)
        print(right)

        # 왼쪽에 남는 요소가 있는지 확인

        while i < len(left) :
            arr[k] = left[i]

            i +=1
            k +=1

        # 오른쪽에 남는 요소가 있는지 확인

        while j < len(right):
            arr[k] = right[j]

            j += 1
            k += 1


def printlist(arr):
    for i in range(len(arr)):
        print(arr[i], end = " ")
    print()



if __name__ == "__main__":
    arr = [7,3,2,16,24,4,11,9]
    print("정렬전 테스트 배열 ",end="\n")
    printlist(arr)

    merge_sort(arr) # 병합정렬 적용

    print("정렬된 테스트 배열 ",end="\n")
    printlist(arr)
