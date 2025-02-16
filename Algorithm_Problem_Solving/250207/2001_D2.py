import sys
sys.stdin = open("2001.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]


    total_kill = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            # 파리 킬
            kill = 0
            # 파리채
            for k in range(M):
                for p in range(M):
                    kill += arr[i+k][j+p]

            # 최다킬 경신
            if kill > total_kill:
                total_kill = kill


    print(f'#{tc} {total_kill}')
