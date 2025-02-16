def seq_search(a, n, key):
    for i in range(n):
        if a[i] == key:
            return i
        elif a[i] > key:
            return -1
    return -1

arr = [2, 4, 7, 9, 11, 19, 23]


print(seq_search(arr, len(arr), 11))