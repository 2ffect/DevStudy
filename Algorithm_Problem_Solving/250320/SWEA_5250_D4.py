# 최소 비용
import sys
sys.stdin = open('5250_input.txt')
import heapq

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def dijkstra():

    dists = [[float('inf')] * N for _ in range(N)]
    dists[0][0] = 0  # 시작점 초기화

    pq = [(0, 0, 0)]  # (dist - 누적거리, y, x) 형태

    while pq:
        dist, i, j = heapq.heappop(pq)

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            # 유효 할 때
            if (0 <= ni < N) and (0 <= nj < N):
                # 출발점과 다음 위치의 높이가 같으면 (평지면)
                if graph[i][j] == graph[ni][nj]:
                    new_dist = dist + 1
                # 오르막이면
                elif graph[ni][nj] > graph[i][j]:
                    new_dist = dist + (graph[ni][nj] - graph[i][j]) + 1
                # 내리막이면
                elif graph[i][j] > graph[ni][nj]:
                    new_dist = dist + 1

                # 이미 더 작거나 같은 거리로 온 적이 있으면 스킵
                if dists[ni][nj] <= new_dist:
                    continue

                dists[ni][nj] = new_dist
                heapq.heappush(pq, (new_dist, ni, nj))

    return dists[N - 1][N - 1]

for tc in range(1, int(input()) + 1):
    # 받아올 배열의 칸(노드의 수라고 생각)
    N = int(input())

    graph = [list(map(int, input().split())) for _ in range(N)]

    result = dijkstra()

    print(f'#{tc} {result}')