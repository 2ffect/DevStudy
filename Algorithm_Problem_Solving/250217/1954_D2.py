# 달팽이 숫자

# 1차 시도 - 제한 시간 70분
# 시작 시간 : 02/17 11:30
# 종료 시간 : 02/17 12:40 실패

# 2차 시도
# 시작 시간 : 02/17 19:00
# 종료 시간 : 02/17 20:23 실패 망할 달팽이 등껍질 조심해라.



import sys
sys.stdin = open("1954_input.txt", "r")

T = int(input())

for tc in range(1):
    N = int(input())
    arr = [list([0] * N) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    i = 0
    j = 0
    d = 0
    cnt += 1

    while cnt <= N*N:
        ni = i + di[d]
        nj = j + dj[d]
        if (0 <= ni < N) and (0 <= nj < N) and arr[i][j] == 0:
            i = ni
            j = nj
            arr[ni][nj] = cnt
            cnt += 1
        else:
            d = (d + 1) % 4

    print(f'{tc}')
    print(arr)