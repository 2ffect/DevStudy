# import sys
# sys.stdin = open("2001.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    k_f =0

    for i in range(N-1):
        for j in range(N-1):
            s = arr[i][j]
            for di, dj in [[0, 1], [1, 1], [1, 0]]:
                for d in range(1, M+1):
                    ni = di + (d * M)
                    nj = dj + (d * M)

                    if (0 <= ni < N-1) and (0 <= nj < N-1):
                        s += arr[ni][nj]

            if s > k_f:
                k_f = s

    print(f'{tc} {k_f}')
