# 미로 1
# 제한 시간 - 점시시간 전 까지 1시간 30분 ?

# 시작 시간 : 02/20 11:07
# 종료 시간 : 02/20 11:30 성공

# 모두 크기가 16*16으로 동일한 미로가 테스트 케이스 마다 주어진다.
# 출발점 2 에서 탈출구 3 까지 갈 수 있다면 1, 다면 0 을 리턴한다.

# 1. 출발점을 찾는다.
# 2. bfs를 통해 탐색하며 3을 만난다면 1을 리턴하고 탈출
# 3. 모든 순회를 마쳤음에도 3을 만나지 못 했다면 해당 미로는 탈출할 수 없으므로 0을 리턴,
from collections import deque

import sys
sys.stdin = open("1226_input.txt", "r")


# bfs 생성
# i, j = 출발점의 좌표, N = 미로의 크기
def bfs(i, j, N):
    # visited 만들기
    # 2차원 배열로 N 크기만큼 0으로 채워서
    visited = [[0] * N for _ in range(N)]
    # 큐 생성
    q = deque()
    # 인큐
    q.append([i, j])
    # 인큐 표시
    visited[i][j] = 1
    # 반복 조건, 큐가 텅텅 빌 때 까지
    while q:
        # 디큐, t 에담기
        ti, tj = q.popleft()
        # t를 활용, maze[ti][tj]가 3이라면 미로를 탈출할 수 있으므로, 1을 리턴해라.
        if maze[ti][tj] == '3':
            return 1
        # t 에 접한 w에 방문한 적없으면, 인큐하고 인큐 표시하기
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti + di, tj +dj
            # 유효하면서, 벽이 아니면서, 방문한 적 없으면, 인큐하고, 방문확인.
            if (0 <= wi < N) and (0 <= wj <N) and maze[wi][wj] != '1' and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = visited[ti][tj] + 1

    # t를 활용, maze[ti][tj]에서 3을 찾을 수 없으면, 탈출할 수 없다. 0을 리턴해라.
    else:
        return 0

# 출발점 찾기
def start_point(N):
    for i in range(N):
        for j in range(N):
            # 주어진 배열을 순회하며 [i][j]가 2일 경우 출발점으로 리턴해준다.
            if maze[i][j] == '2':
                return  i, j

# 미로의 크기는 모두 동일
N = 16

# 테케 별 인풋 받기
for _ in range(10):
    # tc 받아오기
    tc = int(input())
    # 미로 받아오기
    # 숫자를 활용하지 않기 때문에 str로 받아 온다.
    maze = [input() for _ in range(N)]

    # 스타트 포인트 찾기
    sti, stj = start_point(N)

    # bfs 탐색 하여 결과 받기.
    result = bfs(sti, stj, N)

    print(f'#{tc} {result}')