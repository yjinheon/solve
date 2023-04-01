# 퀵소트 case 2 

def quick_sort(array):
    arr_length = len(array)

    if (arr_length <= 1):
        return array
    else:
        pivot = array[0]

        gt = [element for element in array[1:] if element > pivot]
        ls = [element for element in array[1:] if element <= pivot]

        return quick_sort(ls) + [pivot] + quick_sort(gt)


test_array = [54,26,93,17,77,31,44,55,20]



if __name__ == "__main__":
    print(quick_sort(test_array))

