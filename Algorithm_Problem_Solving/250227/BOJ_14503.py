# 로봇 청소기

# 방의 크기 N * M
N, M = map(int, input().split())
# 청소기 초기 위치와 머리 방향
i, j, d = map(int, input().split())
# 방 상태 1 = 벽, 0 = 청소가 되어있지 않은 구역
room = [list(map(int, input().split())) for _ in range(N)]

# 청소기의 델타 방향
# d = 0 = 북쪽 / d = 1 = 동쪽 / d = 2 = 남쪽 / d = 3 = 서쪽
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 청소 횟수
clean_cnt = 0

# 종료조건 발생 시 까지 반복
while True:
    # 청소기의 위치가 0 이면 청소 진행 후 횟수 추가
    if room[i][j] == 0:
        room[i][j] = -1
        clean_cnt += 1


    # 아니라면, 탐색 반 시계 방향으로
    for _ in range(4):
        d = (d - 1) % 4

        # 청소기의 다음 탐색지점 갱신
        ni = i + di[d]
        nj = j + dj[d]


        # 다음 위치가 유효하다고 청소가 가능하면
        if (0 <= ni < N) and (0 <= nj < M) and room[ni][nj] == 0:
            # 좌표 옮기고 for문 탈출
            i, j = ni, nj
            break

        # 다음 위치가 유효한데 이미 청소가 되어 있다면
        elif (0 <= ni < N) and (0 <= nj < M) and room[ni][nj] == -1:
            continue

    # 4 방향 모두 청소가 불가능 하다면
    else:
        # 후진
        ni = i - (di[d])
        nj = j - (dj[d])
        # 유효하고 벽이 아니라면
        if (0 <= ni < N) and (0 <= nj < M) and room[ni][nj] != 1:
            i, j = ni, nj

        # 벽이라면
        elif (0 <= ni < N) and (0 <= nj < M) and room[ni][nj] == 1:
            break

print(clean_cnt)