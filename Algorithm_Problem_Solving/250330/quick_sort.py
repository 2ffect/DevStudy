def partitioning(left, right):
    pivot = arr[left]

    i = left + 1
    j = right

    while i <= j:
        # 큰값 찾기
        while i <= j and arr[i] <= pivot:
            i += 1

        # 작은 값 찾기
        while i <= j and arr[j] >= pivot:
            j -= 1

        # 스왑
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]

    # 피봇 위치값 리턴
    return j



def quick_sort(left, right):
    if left < right:
        pivot = partitioning(left, right)

        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)

arr = [3, 2, 4, 6, 9, 1, 8, 7, 5]
quick_sort(0, len(arr) - 1)
print(arr)