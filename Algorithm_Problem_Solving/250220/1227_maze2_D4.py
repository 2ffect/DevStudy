# 미로 2

# 제한 시간 - 1시간
# 시작 시간 : 02/20 11:33
# 종료 시간 : 02/20 11:50 성공

# 크기가 100 * 100 으로 고정된 미로가 테스트 케이스 마다 주어진다.
# 출발점에서 도착점까지 갈 수 있는지 판단하는 프로그램을 작성하라
# 도달 가능하다면 1, 불가능 하다면 0 을 출력

# 1. 출발점을 찾는다.
# 2. bfs로 탐색한다.
# 3. 출발점에서 탐색하여 탈출 가능하면 1 불가능하면 0 을 리턴한다.

from collections import deque
import sys
sys.stdin = open("1227_input.txt","r")

# 미로의 크기 100 * 100 으로 고정
N = 100

# 출발점 찾기
def start_point(N):
    for i in range(N):
        for j in range(N):
            # 출발점을 찾으면 좌표를 리턴
            if maze[i][j] == '2':
                return i, j

# bfs
def bfs(i, j, N):
    # 방문목록 생성
    visited = deque([0] * N for _ in range(N))
    # 큐 생성
    q = deque()
    # 인큐
    q.append([i, j])
    # 방문목록에 작성
    visited[i][j] = 1
    # 큐가 empty 될 때 까지 탐색
    while q:
        # 디큐해서 가져오기
        ti, tj = q.popleft()
        # 탈출 가능하면 1 리턴
        if maze[ti][tj] == '3':
            return 1
        # 인접한 곳들이 유효하면서, 벽이 아니고, 방문한 적 없으면 인큐
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti + di, tj + dj
            if (0 <= wi < N) and (0 <= wj < N) and maze[wi][wj] != '1' and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1

    # 탈출 불가능 하면 0 리턴
    return 0



for _ in range(10):
    # 테케 번호 받기
    tc = int(input())
    # 미로 받기
    maze = [input() for _ in range(N)]

    # 출발점 좌표 찾기
    sti, stj = start_point(N)
    # 미로 탐색
    result = bfs(sti, stj, N)

    print(f'#{tc} {result}')