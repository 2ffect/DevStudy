import sys
sys.stdin = open("1209.txt", "r")

T = 10
for tc in range(1, T+1):
    tc_num = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # real_max = 0
    max_sum = []

    # i 기준 별 합 중 가장 높은 값을 max_v 에 넣기
    for i in range(100):
        low_sum = 0
        for j in range(100):
            low_sum += arr[i][j]

        # if low_sum >= max_sum:
        #     max_sum = low_sum

        max_sum.append(low_sum)

    # j 기준 별 합 중 가장 높은 값이 max_v 보다 높으면 교체
    for j in range(100):
        col_sum = 0
        for i in range(100):
            col_sum += arr[i][j]

        # if col_sum >= max_sum:
        #     max_sum = col_sum

        max_sum.append(col_sum)

    # 대각선 정방향 기준 합이 max_v 보다 높으면 교체
    iej_sum = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                iej_sum += arr[i][i]

        # if iej_sum >= max_sum:
            # max_sum = iej_sum

        max_sum.append(iej_sum)

    # 대각선 역방향 기준 합이 max_v 보다 높으면 교체
    rev_sum = 0
    for i in range(100):
        for j in range(100):
            if 100-1-i == j:
                rev_sum += arr[i][100-1-i]

        # if rev_sum > max_sum:
            # max_sum = rev_sum

        max_sum.append(rev_sum)

    result = max(max_sum)

    print(f'#{tc_num} {result}')

