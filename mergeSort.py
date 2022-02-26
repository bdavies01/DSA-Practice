def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_half = arr[:mid]
        right_half = arr[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

if __name__ == "__main__":
    arrToSortEven = [5, 222, 432, 2, 39, 401, 1, 888, 292, 883, 132, 6] #12
    arrToSortOdd = [5, 2, 7, 2, 39, 401, 1, 888, 292, 883, 132] #11
    mergeSort(arrToSortOdd)
    print(arrToSortOdd)
