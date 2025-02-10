def binarysearch(a, n, key):    # key를 찾으면 인덱스 , 실패하면 -1 반환
    start = 0
    end = n-1
    while start <= end:         # 검색 구간에 1개 이상의 원소가 있으면 검색 수행
        middle = (start + end) // 2
        if a[middle] == key:    # 검색 성공 인덱스 리턴
            return middle
        elif a[middle] > key:   # 키보다 크면 왼쪽 구간 선택
            end = middle - 1
        else:                   # a[middle] < key, 키보다 작으면 오른쪽 구간 선택
            start = middle + 1
    return -1                   # 검색구간이 남아 있지 않으면 검색 실패 (찾는 값이 없는 경우)

arr = [2, 4, 7, 9, 11, 19, 23]

print(binarysearch(arr, len(arr), 19))      # 5
print(binarysearch(arr, len(arr), 100))     # -1
print(binarysearch(arr, len(arr), 1))       # -1