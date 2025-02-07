import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/JH/sum.txt", "r")

T = 10
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_sum = 0
    # i 기준 별 합 중 가장 높은 값을 max_v 에 넣기
    for i in range(100):
        low_sum = 0
        for j in range(100):
            low_sum += arr[i][j]

        if low_sum >= max_sum:
            max_sum = low_sum



    # j 기준 별 합 중 가장 높은 값이 max_v 보다 높으면 교체
    for j in range(100):
        col_sum = 0
        for i in range(100):
            col_sum += arr[i][j]

        if col_sum > max_sum:
            max_sum = col_sum


    # 대각선 정방향 기준 합이 max_v 보다 높으면 교체


    # 대각선 역방향 기준 합이 max_v 보다 높으면 교체
