import sys
sys.stdin = open('graph.txt')

import heapq

def prim(start_node):

    # 시작점의 가중치는 0, 시작 노드
    my_q = [(0, start_node)]
    # visited 역할
    MST = [0] * V
    # 최소 비용 저장
    min_weight =0

    while my_q:
        weight, node = heapq.heappop(my_q)

        # 이미 방문한 노드를 뽑았다면 continue
        if MST[node]:
            continue
        # 아니라면 방문처리
        MST[node] = 1
        # 누적합을 추가
        min_weight += weight

        for next_node in range(V):
            if graph[node][next_node] == 0:
                continue

            if MST[next_node] == 1:
                continue

            heapq.heappush(my_q, (graph[node][next_node], next_node))

    return min_weight

# 정점수 / 간선수
V, E = map(int, input().split())
graph = [[0] * V for _ in range(V)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = weight
    # 양방향
    graph[end][start] = weight

# 시작 정점을 바꾸어도 결과가 동일하게 보장된다.
# 그렇기 때문에 그리디로 접근 가능
result = prim(0)

print(result)