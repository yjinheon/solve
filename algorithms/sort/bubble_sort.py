
test_arr = [54,26,93,17,77,31,44,55,20]

def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j]
        if not swapped:
            break

    return arr

if __name__ == "__main__":
    print("Sorted array is:")
    for i in bubble_sort(test_arr):
        print(i,end=" ")