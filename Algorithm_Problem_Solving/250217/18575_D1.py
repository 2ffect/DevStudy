# 풍선팡 보너스 게임

# 1차 시도
# 시작 시간 : 02/17 16:00
# 종료 시간 : 02/18 17:10 성공

import sys
sys.stdin = open("18575_input.txt", "r")


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_sum = 0
    min_sum = 100000

    for i in range(N):
        for j in range(N):
            point = 0
            # 4방향으로
            for d in range(4):
                # 다른 방향으로 갈 때 본인은 더해지지 않아야 함
                if d != 0:
                    point -= arr[i][j]
                # 끝까지
                for c in range(N):
                    ni = i + (di[d] * c)
                    nj = j + (dj[d] * c)
                    # 유효할 때
                    if (0 <= ni < N) and (0 <= nj < N):
                            # point에 다 더해준다.
                            point += arr[ni][nj]

            if max_sum < point:
                max_sum = point
            if min_sum > point:
                min_sum = point

    result = max_sum - min_sum

    print(f'#{tc} {result}')