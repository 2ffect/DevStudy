# 파리퇴치 3

# 시작 시간 : 02/27 16:20
# 종료 시간 : 02/27 16:40

import sys
sys.stdin = open("12712_input.txt","r")

T = int(input())

for tc in range(1, T+1):
    # N : 배열의 크기 / M : 스프레이 범위
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 1번 스프레이 +
    di_1 = [0, 1, 0, -1]
    dj_1 = [1, 0, -1, 0]

    # 2번 스프레이 x
    di_2 = [-1, 1, 1, -1]
    dj_2 = [1, 1, -1, -1]

    max_kill = 0

    # 1번 스프레이로 순회하며 최다킬 계산
    for i in range(N):
        for j in range(N):
            kill_1 = arr[i][j]
            for d in range(4):
                for m in range(1, M):
                    ni = i + di_1[d] * m
                    nj = j + dj_1[d] * m
                    # 유효하면 사냥 가능 kill_1에 더해주기
                    if (0 <= ni < N) and (0 <= nj <N):
                        kill_1 += arr[ni][nj]

            # kill_1 이 max_kill 보다 크면 갱신
            if max_kill < kill_1:
                max_kill = kill_1

    # # 2번 스프레이로 순회하며 최다킬 계산
    for k in range(N):
        for p in range(N):
            kill_2 = arr[k][p]
            for d in range(4):
                for s in range(1, M):
                    ni = k + di_2[d] * s
                    nj = p + dj_2[d] * s
                    if (0 <= ni < N) and (0 <= nj < N):
                        kill_2 += arr[ni][nj]

            if max_kill < kill_2:
                max_kill = kill_2

    print(f'#{tc} {max_kill}')