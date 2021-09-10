# Hoare Partition Quick Sort
# https://www.youtube.com/watch?v=5iSZ7mh_RAk&t=723s

def hoarePartition(arr, left, right):
    pivot = arr[left]
    start = left + 1
    end = right

    while start <= end:
        if arr[start] <= pivot:
            start += 1
        elif arr[end] > pivot:
            end -= 1
        else:
            arr[start], arr[end] = arr[end], arr[start]

    # swap pivot with element at end
    arr[left], arr[end] = arr[end], arr[left]
    return end


def quickSort(arr, left, right):
    if left < right:
        p = hoarePartition(arr, left, right)
        # print(p)
        quickSort(arr, left, p - 1)
        quickSort(arr, p + 1, right)


if __name__ == '__main__':
    lst = [11, 9, 2, 7, 29, 15, 28]
    # p = hoarePartition(lst, 0, len(lst) - 1)
    # print("Index of pivot:", p)
    # print(lst)
    print("--" * 30)
    print("After Quick Sort")
    quickSort(lst, 0, len(lst) - 1)
    print(lst)
