# 로봇 청소기

# 방의 크기 N * M
N, M = map(int, input().split())
# 청소기 초기 위치와 머리 방향
I, J, D = map(int, input().split())
# 방 상태 1 = 벽, 0 = 청소가 되어있지 않은 구역
room = [list(map(int, input().split())) for _ in range(N)]

# 청소기의 델타 방향
# d = 0 = 북쪽 / d = 1 = 동쪽 / d = 2 = 남쪽 / d = 3 = 서쪽
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

# 청소 횟수
clean_cnt = 0

i, j, d = I, J, D

# 청소 할 구역이 없을 때 까지 계속 진행
while True:
    # 청소기의 위치에 청소가 되어있지 않은 경우,
    if room[i][j] == 0:
        # 청소를 진행한다. 현재 위치 상태를 0에서 -1로 바꾼다.
        room[i][j] = -1
        # 청소 횟수를 1회 증가 시킨다.
        clean_cnt += 1
        # 청소 후 머리 돌려주기
        d = (d - 1) % 4

    # 이동 한 구간이 이미 청소 된 경우, 해당 구역에서 재탐색
    elif room[i][j] == -1:
        d = (d - 1) % 4

    # 탐색 한 좌표
    ni = i + di[d]
    nj = j + dj[d]
    # 유효하면서 청소가 되어있지 않은 경우
    if (0 <= ni < N) and (0 <= nj < M) and room[ni][nj] == 0:
        # 청소기를 이동 시킨 후 청소를 하러 간다.
        i, j = ni, nj
        continue

    # 유효한데, 청소할 곳이 없는 경우 == 후진을 해야한다.
    elif (0 <= ni < N) and (0 <= nj < M) and room[ni][nj] != 0:
        # ni, nj를 후진 한 위치로 새로 정의
        ni = i - di[d]
        nj = j - dj[d]
        # 다시 유효성 검사 진행, 후진한 위치가 벽이 아닐 경우,
        if (0 <= ni < N) and (0 <= nj < M) and room[ni][nj] != 1:
            # 후진 위치로 청소기를 이동시킨 후 청소하러 간다.
            i, j = ni, nj
            continue
        # 만약 후진한 위치가 벽이라면, 청소를 종료한다.
        elif (0 <= ni < M) and (0 <= nj < N) and room[ni][nj] == 1:
            # break for while True
            break

# 청소가 끝났다면 청소 횟수를 출력한다.
print(clean_cnt)