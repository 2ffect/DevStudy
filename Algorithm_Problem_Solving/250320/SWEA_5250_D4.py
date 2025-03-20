# 최소 비용
# 그리디 bfs 프림으로 모든 정점의 최소비용을 다 확인..

import sys
sys.stdin = open('5250_input.txt')
import heapq

def prim(start_v):

    # 시작점의 가중치는 0
    my_q = [(1, start_v)]
    MST = [0] * N
    # 최소 비용 저장
    min_weight = 0


    while my_q:
        weight, node = heapq.heappop(my_q)

        # 이미 방문한 노드를 뽑았다면 스킵
        if MST[node]:
            continue
        # 아니라면 방문처리
        MST[node] = 1

        min_node = 9999999
        else_node = 0
        for next_node in range(N):
            a = graph[node][next_node]
            b = graph[node][node]
            c = a - b
            if c > 0:
                min_node = min(min_node, c)

            else:
                else_node += 1

            if MST[next_node] == 1:
                continue

            heapq.heappush(my_q, (graph[node][next_node], next_node))

        else:
            if min_node != 99999999:
                min_weight += min_node + else_node
            else:
                min_weight += else_node

    return min_weight

for tc in range(1, int(input()) + 1):
    # 받아올 배열의 칸(노드의 수라고 생각)
    N = int(input())

    graph = [list(map(int, input().split())) for _ in range(N)]

    result = prim(0)

    print(f'#{tc} {result}')