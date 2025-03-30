import sys
sys.stdin = open('sample_input(2).txt')

def merge_sort(li):
    if len(li) == 1:
        return li

    mid = len(li)//2
    left = li[:mid]
    right = li[mid:]

    left_li = merge_sort(left)
    right_li = merge_sort(right)

    merge_list = merge(left_li, right_li)
    return merge_list

def merge(left, right):
    global cnt
    result = [0] * (len(left) + len(right))
    l = r = 0

    if left[-1] > right[-1]:
        cnt += 1

    while (l < len(left)) and (r < len(right)):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r <len(right):
        result[l + r] = right[r]
        r += 1

    return result

for tc in range(1, int(input()) + 1):
    N = int(input())
    M = N//2
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arr)

    print(f'#{tc} {result[M]} {cnt}')