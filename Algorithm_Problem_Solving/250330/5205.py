import sys
sys.stdin = open('sample_input(3).txt')

def partitioning(left, right):
    pivot = arr[left]
    i = left + 1
    j = right

    while i <= j:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j], arr[left]
    return j

def quick_sort(left, right):
    if left < right:
        pivot = partitioning(left, right)

        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)

for tc in range(1, int(input()) + 1):
    N = int(input())
    M = N // 2
    arr = list(map(int, input().split()))
    quick_sort(0, N-1)
    result = arr[M]
    print(f'#{tc} {result}')