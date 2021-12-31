"""
- https://github.com/minsuk-heo
- 2016

performance : O(nlogn) , worst case O(n^2)
space complexity : O(n) # 따로 메모리를 사용하지 않고 현재 메모리 안에서 정렬

- pivot 정하기
- pivot보다 작을 경우 왼쪽, 클경우 오른쪽

"""

def quick_sort(list,start,end):
    if start < end:
        # get pivot using partition method
        pivot = partition(list,start,end)
        # recursive quick sort left side from pivot
        quick_sort(list, start,pivot-1)

        quick_sort(list,pivot+1,end)
        # recursive quick sort right side fro, pivot

    return list


def partition(list,start,end):
    # use end item as inital pivot

    pivot = end

    wall = start

    left = start

    while left < pivot:
        # 왼쪽이 pivot보다 작을 경우 wall과 swap하고 wall을 오른쪽으로 옮김
        # pivot보다 작은 item이 wall의 왼쪽으로 유지되게끔 함
        # pivot보다 큰 item은 wall의 오른쪽

        if list[left] < list[pivot] :
            list[wall] , list[left] = list[left] , list[wall]

            wall = wall + 1 # wall오른쪽으로 옮김
        left = left +1

    # when left hit the end of the list , swap pivot with wall
    list[wall], list[pivot] = list[pivot] , list[wall]

    pivot = wall # wall is new pivot

    return pivot



def quicksort(x): # 위키피디아 버전
    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return quicksort(less) + equal + quicksort(more)



if __name__ == "__main__":
    test_list = [8,3,2,6,1,4]
    print(quick_sort(test_list,0,len(test_list)-1))


