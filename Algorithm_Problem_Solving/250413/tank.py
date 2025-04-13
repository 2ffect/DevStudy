import sys
from collections import deque
sys.stdin = open('test.txt')
N = 8
battlefield = [input().split() for _ in range(N)]

# 탱크 = A 포탑 = H
# 포탄 사거리 : 3
# 풀 = G (지나갈 수 있음) / 물 = W (지나갈 수 없음)

# 탱크 찾기
def find_tank(N):
    for i in range(N):
        for j in range(N):
            # 탱크 찾으면 좌표 리
            if battlefield[i][j] == 'A':
                return i, j

# bfs
# i, j = 탱크좌표, N = 출발점
def bfs(i, j):
    # 방문표시
    visited = [[0] * N for _ in range(N)]
    # 큐 생성 / 인큐
    q = deque()
    q.append([i,j])
    # 방문 표시
    visited[i][j] = 1
    while q:
        # 디큐
        ti, tj = q.popleft()
        # 디큐 좌표가 적 포탑이라면 해당 거리를 리턴
        if battlefield[ti][tj] == 'X':
            return visited[ti][tj]

        # 인접에 방문하지 않았다면 방문 기록하고 인큐
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti + di, tj + dj
            # 유효하면서, 방문한 적 없고, G일 경우(잔디)만 방문가능.
            if (0 <= wi < N) and (0 <= wj < N) and battlefield[wi][wj] == 'G' and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1
            elif (0 <= wi < N) and (0 <= wj < N) and battlefield[wi][wj] == 'X':
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1

    # 적 포탑에 도달할 수 없다면 -1 을 리턴
    else:
        return -1

# 탱크 위치
tank_i, tank_j = find_tank(N)
# bfs 활용 적 포탑 탐색
enemy = bfs(tank_i, tank_j)
