# 미로 1

# 출발점은 2, 도착점은 3, 길은 0, 벽은 1
# 출발점에서 도착점까지 도달 가능하면 1, 아니면 0을 리턴
import sys
sys.stdin = open('1226_input.txt')

from collections import deque

# 출발점 찾기
def start_point(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j

# i, j 출발점 좌표
# N : 맵 크기
def bfs(i, j, N):
    # 방문기록
    visited = [[0] * N for _ in range(N)]
    # 큐 생성
    my_q = deque()
    # 인큐
    my_q.append([i, j])
    # 방문 기록
    visited[i][j] = 1
    while my_q:
        ti, tj = my_q.popleft()
        # 디큐 값이 도착점이면 1을 리턴
        if maze[ti][tj] == '3':
            return 1

        # 현재 위치에서 4방향 탐색
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = ti + di, tj + dj
            # 유효하고, 1이 아니고, 방문한 적 없으면 방문기록 후 인큐
            if (0 <= ni < N) and (0 <= nj < N) and maze[ni][nj] != '1' and visited[ni][nj] == 0:
                my_q.append([ni, nj])
                visited[ni][nj] = visited[ti][tj] + 1

    # 전부 확인 했는데 탈출구를 못 찾았으면 0을 리턴
    return 0

N = 16
for _ in range(1, 11):
    tc = int(input())
    maze = [input() for _ in range(N)]

    # 출발점 찾기
    start_i, start_j = start_point(N)
    # bfs 탐색
    result = bfs(start_i, start_j, N)

    print(f'#{tc} {result}')