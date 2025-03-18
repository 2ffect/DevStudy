# # 1. 분할 : 리스트의 길이가 1일 때 까지
# # 2. 정복 : 리스트의 길이가 1이되면 자동으로 정렬되는 것
# # 3. 병합 :
# #   - 왼쪽, 오른쪽 리스트 중
# #       작은 원소부터 정답 리스트에 추가하면서 진행
#
def merge(left, right):
    # 두 리스트를 병합한 결과 리스트
    result = [0] * (len(left) + len(right))
    # 왼쪽/오른쪽 빠른 인덱스 지정
    l = r = 0

    # 두 리스트에서 비교할 대상이 남아있을 때 까지 반복
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


def merge_sort(li):

    # li 길이가 1이 될 때 까지
    if len(li) == 1:
        return li

    # 1. 절반씩 분할
    mid = len(li) // 2
    # 리스트의 왼쪽 절반
    left = li[:mid]
    # 리스트의 오른쪽 절반
    right = li[mid:]

    left_li = merge_sort(left)
    right_li = merge_sort(right)
    # 분할이 완료되면
    # 2. 병합
    merged_li = merge(left_li, right_li)
    return merged_li

arr = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_arr = merge_sort(arr)
print(sorted_arr)