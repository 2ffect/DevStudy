import sys
from collections import deque

sys.stdin = open('test.txt')
N = 8
battlefield = [input().split() for _ in range(N)]

# 탱크 찾기
def find_tank(N):
    for i in range(N):
        for j in range(N):
            if battlefield[i][j] == 'A':
                return i, j

# bfs
def bfs(i, j):
    visited = [[0] * N for _ in range(N)]
    prev = [[None] * N for _ in range(N)]  # 이전 위치 저장
    q = deque()
    q.append([i, j])
    visited[i][j] = 1

    while q:
        ti, tj = q.popleft()
        if battlefield[ti][tj] == 'X':
            # 경로 추적
            path = []
            ci, cj = ti, tj
            while (ci, cj) != (i, j):
                path.append((ci, cj))
                ci, cj = prev[ci][cj]
            path.append((i, j))
            path.reverse()
            return visited[ti][tj], path

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti + di, tj + dj
            if 0 <= wi < N and 0 <= wj < N and visited[wi][wj] == 0:
                if battlefield[wi][wj] == 'G' or battlefield[wi][wj] == 'X':
                    q.append([wi, wj])
                    visited[wi][wj] = visited[ti][tj] + 1
                    prev[wi][wj] = (ti, tj)

    return -1, []  # 도달 실패

# 실행
tank_i, tank_j = find_tank(N)
enemy, path = bfs(tank_i, tank_j)
print(enemy)
if path:
    print(path)