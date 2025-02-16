def seq_scaerch(a, n, key):
    for i in range(n):
        if a[i] == key:
            return i
    return -1

arr = [4, 9, 11, 23, 2, 19, 7]

# 2를 검색하는 경우
print(seq_scaerch(arr, len(arr), 2))


