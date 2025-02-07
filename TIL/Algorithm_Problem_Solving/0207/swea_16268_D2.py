import sys
sys.stdin = open("16268.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 상 하 좌 우 1칸씩
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    max_flower = 0

    for i in range(N):
        for j in range(M):
            # 기준점 지정 (나)
            flower = arr[i][j]
            # 내 기준으로 4방향 1칸씩
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                # 유효 할 때
                if 0 <= ni < N and 0 <= nj < M:
                    # 다 더해
                    flower += arr[ni][nj]
            # 최대 꽃가루 보다 크면 대장
            if flower >= max_flower:
                max_flower = flower

    print(f'#{tc} {max_flower}')
