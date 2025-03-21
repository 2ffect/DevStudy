# 최소 이동 거리

import sys
sys.stdin = open('5251_input.txt')
import heapq

def dijkstra(v):
    # 큐 생성 및 인큐
    my_q = [(0, v)]
    # 각 정점별 최단 거리를 저장할 리스트
    dists = [[float('inf')] * (N+1) for _ in range(N+1)]
    # 시작점은 0으로 초기화
    dists[v][v] = 0

    while my_q:
        dist, node = heapq.heappop(my_q)

        # 이미 더 작은 가중치로 방문했거나 지금 경로가 기존 가중치보다 크면 스킵
        if dists[node] < dist:
            continue

        # 인접 정보를 하나씩 가져와 비교
        for adj in adj_list[node]:
            # 다음 노드로 가기위한 가중치, 다음 노드번호
            next_dist, next_node = adj

            # 다음 노드로 가기위한 누적 가중치
            total_weight = dist + next_dist

            # 가중치가 같거나, 더 작은 가중치로 방문한 기록이 있다면 스킵
            if dists[next_node] <= total_weight:
                continue

            # 아니라면 갱신
            dists[next_node] = total_weight
            heapq.heappush(my_q, (total_weight, next_node))

    # 마지막 노드의에 해당하는 값을 리턴
    return dists[N]

for tc in range(1, int(input()) + 1):
    # 마지막 노드 번호, 간선의 수
    N, E = map(int, input().split())
    # 시작 노드는 0
    start_node = 0
    # 인접 리스트
    adj_list = [[] for _ in range(N+1)]

    # 인접리스트 삽입
    for _ in range(E):
        start, end, weight = map(int, input().split())
        adj_list[start].append((weight, end))

    result = dijkstra(start_node)
    print(f'#{tc} {result}')