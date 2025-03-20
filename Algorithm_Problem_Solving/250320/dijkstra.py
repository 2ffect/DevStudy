import sys
sys.stdin = open('graph2.txt')

import heapq
inf = int(21e8) # 무한대를 의미한다고 가정

def dijkstra(start_node):
    # 누적거리, 노드번호 큐 생성 밑 인큐
    pq = [(0, start_node)]
    # 각 정점별 최단거리를 저장할 리스트
    dists = [inf] * V
    # 시작점은 0으로 초기화
    dists[start_node] = 0

    while pq:
        dist, node = heapq.heappop(pq)

        # 이미 더 작은 경로로 방문한 적 있다면,
        # 지금 가려고 하는 경로가 기존 저장해 둔 경로보다 크다면, 스킵
        if dists[node] < dist:
            continue

        for next_info in graph[node]:
            print(next_info)
            # 다음 노드로 가기위한 가중치, 다음 노드 번호 가져오기
            next_dist, next_node = next_info

            # 다음 노드로 가기위한 누적거리
            new_dist = dist + next_dist

            # 이미 같은 가중치거나, 더 작은 가중치로 방문한 기록이 있다면 스킵
            if dists[next_node] <= new_dist:
                continue

            # next_node 까지 도착하는데 비용은 new_dist
            dists[next_node] = new_dist
            heapq.heappush(pq, (new_dist, next_node))

    return dists

V, E = map(int, input().split())
start_node = 0 # 문제마다 다름
# 인접 리스트
graph = [[] for _ in range(V)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    # 단방향
    graph[start].append((weight, end))

# result_dist : 0 에서 출발해 다른 노드들 까지의 최단거리를 모두 구한다
result_dist = dijkstra(0)
print(result_dist)