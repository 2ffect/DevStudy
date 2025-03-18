# 병합 정렬
import sys
sys.stdin = open('5204_input.txt')

def merge_sort(li):

    # 리스트의 길이가 모두 1이 될 때까지 반복
    if len(li) == 1:
        return li

    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]

    left_li = merge_sort(left)
    right_li = merge_sort(right)

    merged_li = merge(left_li, right_li)
    return merged_li

def merge(left, right):
    global cnt
    # 두 리스트를 병합한 결과 리스트
    result = [0] * (len(left) + len(right))
    # 왼쪽/오른쪽 빠른 인덱스 지정
    l = r = 0

    # 두 리스트에서 비교할 대상이 남아있을 때 까지 반복
    if left[-1] > right[-1]:
        cnt += 1

    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1
    # 왼쪽 리스트에 남은 데이터를 모두 result 에 추가
    while l < len(left):
        result[l + r] = left[l]
        l += 1
    # 오른쪽 리스트에 남은 데이터를 모두 result 에 추가
    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result


for tc in range(1, int(input()) + 1):
    # 리스트 길이
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    sorted_arr = merge_sort(arr)
    result = sorted_arr[N//2]
    print(f'#{tc} {result}')