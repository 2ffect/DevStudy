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
            # 기준점
            num = arr[i][j]
            # 몇 칸을 추가적으로 볼건지
            for c in range(1, arr[i][j]+1):
                # 기준점에서 4 방향으로
                for d in range(4):
                    ni = i + (di[d] * c)
                    nj = j + (dj[d] * c)

                    if 0 <= ni < N and 0 <= nj < M:
                        num += arr[ni][nj]

            # 최대 값 교체
            if max_num < num:
                max_num = num

    print(f'#{tc} {max_num}')
