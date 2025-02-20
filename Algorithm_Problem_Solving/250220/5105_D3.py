# 미로의 거리
from collections import deque


# bfs
def bfs(i, j, N):
    # visited 생성 - 2차원
    visited = [[0] * N for _ in range(N)]
    # 큐 생성
    q = deque()
    # 시작점 인큐
    q.append([i, j])
    # 시작점 인큐 표시
    visited[i][j] = 1

    # 큐가 empty가 될 때 까지 반복
    while q:
        # 디큐해서 t에 저장
        ti, tj = q.popleft()
        # t 활용, 출구에 도착할 경우 1 아니면 0 을 리턴
        if maze[ti][tj] == '3':
            # return 1
            # but 입구와 출구 사이의 빈칸 수
            return visited[ti][tj] - 2
        # t에 인접한 정점 w가 인큐 되지 않았다면
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti + di, tj + dj
            # 근데 미로를 벗어나지 않고, 벽이 아닐 때
            if (0 <= wi < N) and (0 <= wj < N) and maze[wi][wj] != '1' and visited[wi][wj] == 0:
                # 인큐 & 인큐 표시
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1

    # t 활용, 출구에 도착할 경우 1 아니면 0 을 리턴
    return 0


# 출발점 좌표 찾기
def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j


T = int(input())

for tc in range(1, T + 1):
    # 미로의 크기
    N = int(input())
    # 미로 받아오기
    maze = [input() for _ in range(N)]

    # 출발점 찾기
    sti, stj = find_start(N)
    # bfs 활용
    result = bfs(sti, stj, N)
    print(f'#{tc} {result}')