# 싸피 점핑 미로

def bfs(i, j, N):
    # 방문기록
    visited = [[0] * N for _ in range(N)]
    # 큐 생성
    q = []
    # 인큐
    q.append([i, j])
    # 방문 표시
    visited[i][j] = 1

    # 큐가 모두 빌 때 까지 반복
    while q:
        pi, pj = q.pop(0)

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ti, tj = pi + di, pj + dj
            # 유효하고 1이 아닐 때
            if (0 <= ti < N) and (0 <= tj < N) and maze[ti][tj] != 1:
                # 0 이면, 바로 방문 표시 후 인큐
                if maze[ti][tj] == 0 and visited[ti][tj] == 0:
                    visited[ti][tj] = visited[pi][pj] + 1
                    q.append([ti, tj])

                # 4면 점프대, 델타로 점프시켜서 유효할 때 인큐 + 방문표시
                if maze[ti][tj] == 4:
                    visited[ti][tj] = visited[pi][pj] + 1
                    pi, pj = ti, tj
                    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                        ti, tj = pi + di * 2, pj + dj * 2
                        if (0 <= ti < N) and (0 <= tj < N) and maze[ti][tj] != 1:
                            if maze[ti][tj] == 0 and visited[ti][tj] == 0:
                                visited[ti][tj] = visited[pi][pj] + 1
                                q.append([ti, tj])

                if maze[ti][tj] == 3:
                    visited[ti][tj] = visited[pi][pj] + 1
                    return visited[ti][tj]
    else:
        return -1


def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

T = int(input())

for tc in range(1, T+1):
    # 미로의 크기
    N = int(input())
    # 미로
    maze = [list(map(int, input().split())) for _ in range(N)]

    i, j = find_start(N)

    print(f'#{tc} {bfs(i, j, N)}')

    # 방법 1. 출발점 찾고 bfs 탐색하여 3을 발견 할 때의 최소 방문 그룹의 숫자 출력
    # 방법 2. 출발점 찾고 출발점을 기준으로 계속해서 델타 탐색하며 0이면 좌표 이동, 4면 점프대 활용하면서 3을 찾아 갈 때 까지의 최소 거리를 기록