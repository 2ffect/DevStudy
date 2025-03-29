import sys
sys.stdin = open('dijkstra_input.txt')
import heapq

def dijkstra(start_node):
    my_pq = [(0, start_node)]
    visited = [float('inf') for _ in range(N + 1)]
    visited[start_node] = 0

    while my_pq:
        my_pq.sort()
        # dist, node = my_pq.pop(0)
        dist, node = heapq.heappop(my_pq)
        if visited[node] < dist:
            continue

        for next_dist, next_node in adj_list[node]:
            new_dist = dist + next_dist

            if visited[next_node] <= new_dist:
                continue

            visited[next_node] = new_dist
            # my_pq.append((new_dist, next_node))
            heapq.heappush(my_pq, (new_dist, next_node))

    return visited[N]

for tc in range(1, int(input()) + 1):
    # N = 노드의 마지막 번호, E 간선의 수
    N, E = map(int, input().split())
    adj_list = [[] for _ in range(N + 1)]
    # 인풋받아 바로 인접리스트 작성
    for _ in range(E):
        start, end, dist = map(int, input().split())
        # 단 방향이니까 출발 기준으로만 저장
        adj_list[start].append((dist, end))

    # 0번 부터 출발했을 때 결과 값.
    result = dijkstra(0)

    print(f'#{tc} {result}')