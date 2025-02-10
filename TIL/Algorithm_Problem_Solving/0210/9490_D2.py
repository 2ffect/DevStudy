import sys
sys.stdin = open("9490_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_num = 0
    for i in range(N):
        for j in range(M):
            # 타격점
            num = arr[i][j]
            # num이 1 이면 타격점에서 상하좌우 각 1칸씩
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if num != 1:
                    for c in range(1, N+1):
                        ni = i + (ni * c)
                        nj = j + (nj * c)

                        if 0 <= ni < N and 0 <= nj < M:
                            num += arr[ni][nj]
                if 0 <= ni < N and 0 <= nj < M:
                    num += arr[ni][nj]

            # 최대 값 교체
            if max_num < num:
                max_num = num

    print(f'#{tc} {max_num}')
