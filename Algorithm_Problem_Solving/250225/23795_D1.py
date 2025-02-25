# 우주 괴물

# N*N 의 배열을 입력 받는다.
# 0의 갯수를 센다.
# 괴물의 범위에 포함되는 0만큼 빼준다.
# 괴물의 영역은 벽을 만나기 전까지 계속 뻗는다 벽 = 1

# 시작 시간 : 15:15
# 종료 시간 : 15:39 성공

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 0의 총 개수 구하기
    total_zero = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                total_zero += 1



    # 괴물을 찾고 괴물의 영역 만큼 제거하기
    cnt = 0
    for i in range(N):
        for j in range(N):
            # 괴물이면
            if arr[i][j] == 2:
                # 어느 방향으로 ?
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                    # 어느 만큼 ? 끝까지니까 N 만큼가
                    for c in range(N):
                        ni = i + (di * c)
                        nj = j + (dj * c)
                        # 유효할 경우
                        if (0 <= ni < N) and (0 <= nj <N) and arr[ni][nj] != 2:
                            # 근데 1이면? 브레이크 하고 다른 방향으로 가.
                            if arr[ni][nj] == 1:
                                break
                            else:
                                cnt += 1
    result = total_zero - cnt

    print(f'#{tc} {result}')