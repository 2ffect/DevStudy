# [모의 SW역량 테스트] 탈주범 검거

from collections import deque
import sys
sys.stdin = open('1953_input.txt')
# 0 : 우, 1 : 하, 2 : 좌, 3 : 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

pipe = {
    '1' : [0, 1, 2, 3], # 우, 하, 좌, 상
    '2' : [1, 3],       # 하, 상
    '3' : [0, 2],       # 우, 좌
    '4' : [0, 3],       # 우, 상
    '5' : [0, 1],       # 우, 하
    '6' : [1, 2],       # 하, 좌
    '7' : [2, 3]        # 좌,
}

# bfs
def bfs(r, c, L):
    # 방문 체크
    visited = [[0] * M for _ in range(N)]
    # 큐 생성
    q = deque()
    # 인큐
    q.append([r, c])
    # 방문 표시
    visited[r][c] = 1
    # q가 빌 때 까지 반복
    while q:
        # 팝 해서 하나 가져오기
        pr, pc = q.popleft()

        # 딕셔너리에서 현재 위치에 해당하는 값 가져오기,
        # 델타 탐색 필요 방향
        for i in pipe[pipe_map[pr][pc]]:
            nr = pr + di[i]
            nc = pc + dj[i]
            # 다음 위치가 유효하고 0이 아니면서
            if (0 <= nr < N) and (0 <= nc < M) and pipe_map[nr][nc] != '0':
                # 다음 위치 키가 갖는 값이 나를 향해 열려 있어야 함. (가지고 있어야 함)
                    if i == 0:
                        if 2 in pipe[pipe_map[nr][nc]]:
                            # 방문 기록이 되지 않았을 경우 (첫 방문일때)
                            # 방문 기록 후 인큐
                            if visited[nr][nc] == 0:
                                visited[nr][nc] = visited[pr][pc] + 1
                                q.append([nr, nc])

                    elif i == 1:
                        if 3 in pipe[pipe_map[nr][nc]]:
                            # 방문 기록이 되지 않았을 경우 (첫 방문일때)
                            # 방문 기록 후 인큐
                            if visited[nr][nc] == 0:
                                visited[nr][nc] = visited[pr][pc] + 1
                                q.append([nr, nc])

                    elif i == 2:
                        if 0 in pipe[pipe_map[nr][nc]]:
                            # 방문 기록이 되지 않았을 경우 (첫 방문일때)
                            # 방문 기록 후 인큐
                            if visited[nr][nc] == 0:
                                visited[nr][nc] = visited[pr][pc] + 1
                                q.append([nr, nc])

                    elif i == 3:
                        if 1 in pipe[pipe_map[nr][nc]]:
                            # 방문 기록이 되지 않았을 경우 (첫 방문일때)
                            # 방문 기록 후 인큐
                            if visited[nr][nc] == 0:
                                visited[nr][nc] = visited[pr][pc] + 1
                                q.append([nr, nc])

    return visited



T = int(input())

for tc in range(1):
    # 지도 크기 N * M / 시작점 R, C / L = 탈출 후 경과시간
    N, M, R, C, L = map(int, input().split())
    pipe_map = [list(input().split()) for _ in range(N)]

    a = bfs(R, C, L)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < a[i][j] <= L:
                cnt += 1

    print(f'#{tc} {cnt}')