
def merge_sort(li):
    # 리스트 길이가 1이 될 때까지 나누기
    if len(li) == 1:
        return li

    # 중앙값 설정 후 왼쪽, 오른쪽
    mid = len(li)//2
    left = li[:mid]
    right = li[mid:]

    left_li = merge_sort(left)
    right_li = merge_sort(right)

    # 합치기
    merge_li = merge(left_li, right_li)
    return merge_li

def merge(left, right):
    # 결과를 담을 리스트
    result = [0] * (len(left) + len(right))
    # 왼쪽 오른쪽 값 설정
    l = r = 0

    # 두 리스트를 비교하고 들어갈 애들 먼저 넣기
    while (l < len(left)) and (r < len(right)):
        # left의 l 번째 값이 right의 r 번째 값보다 작으면 먼저 삽입 후 l + 1
        if left[l] < right[r]:
            result[l + r] = left[l]
            l += 1
        else:
            result[l + r] = right[r]
            r += 1

    # 나머지 값 다 넣어주기
    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return result


arr = [69, 10, 30, 2, 16, 8, 31, 22]
sorted_arr = merge_sort(arr)
print(sorted_arr)