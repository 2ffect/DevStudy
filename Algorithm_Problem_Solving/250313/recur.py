#
# arr = ['A', 'B', 'C', 'D', 'E']
# path = []
#
#
# n = 3
# def recur (cnt,start):
#     # n 명을 뽑으면 출력 후 리턴
#     if cnt == n:
#         print(*path)
#         return
#
#     # 5명을 고려해야 한다.
#     for i in range(start, len(arr)):
#         path.append(arr[i])
#         recur(cnt + 1, i + 1)
#         path.pop()
#
#
# recur(0, 0)
#
# 주사위 던지기

arr = [1, 2, 3, 4, 5, 6]
path = []

n = 3

def recur(cnt, start):
    if cnt == n:
        print(path)
        return

    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(cnt + 1, i)
        path.pop()

recur(0, 0)