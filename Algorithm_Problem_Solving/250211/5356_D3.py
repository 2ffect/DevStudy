import sys
sys.stdin = open("5356_input.txt", "r")

# 의석이 세로로 말해요

T = int(input())

for tc in range(1, T+1):
    arr = [list(map(str, input())) for _ in range(5)]

    max_arr = 0
    for i in arr:
        if len(i) > max_arr:
            max_arr = len(i)

    new_list = []

    for j in range(max_arr):
        for i in range(5):
            if len(arr[i]) <= j:
                continue

            new_list.append(arr[i][j])

    result = ''.join(new_list)

    print(f'#{tc} {result}')