N, M = map(int, input().split())   #  N*M 방
i, j, dr = map(int, input().split())  # 현재x좌표 현재y좌표 현재방향
arr = [list(map(int, input().split())) for _ in range(N)]

di = [-1, 0, 1, 0]          # 상 좌 하 우 (반시계방향 회전)
dj = [0, -1, 0, 1]
count = 0


while True:
    if arr[i][j] == 0:   # 처음은 청소 안된칸
        arr[i][j] = 2   # 청소했다고 표시해준다
        count += 1      # 청소 횟수를 올려줌
        # 이제 90도 회전하면서 찾아야하는데
    for k in range(4):
        dr = (dr + 1) % 4  # 반시계 90도 회전해서 방향바꾸고

        ni = i + di[dr]
        nj = j + dj[dr]
        # 해당 좌표가 범위를 안나가고 / 청소도 안됐으면
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            i = ni      # 좌표 갱신 (로청 이동)
            j = nj
            # 카운트,2로변경은 안해줘도됨 왜냐면 break해서 위로돌아가서 어차피 할거니깐
            # 다시 처음으로 돌아간다
            break

        # 다음 위치가 유효한데 이미 청소가 되어 있다면
        elif (0 <= ni < N) and (0 <= nj < M) and arr[ni][nj] == -1:
            continue

    else: # 회전해서 간 칸이 청소 돼있으면
        # 후진할거임.
        i = i - di[dr]
        j = j - dj[dr]
        # 만약 후진을 못하면 break 할거니깐.
        # 만약 벽이거나 튀어나가면;
        if (i >= N or i < 0 or j >= M or j < 0):
            break
        if arr[i][j] == 1:
            # 청소끝.
            break

print(count)
