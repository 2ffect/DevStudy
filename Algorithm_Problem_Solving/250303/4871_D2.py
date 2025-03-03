# 그래프 경로

import sys
sys.stdin = open("4871_input.txt")

# s = 시작 노드 / e = 목적지 노드 / v = 마지막 노드
def dfs(s, e, v):
    # 방문 기록 생성
    visited = [0] * (V+1)
    # 스택 생성
    my_stack = []

    while True:
        # 시작 노드에 방문한 적 없다면 방문 기록
        if visited[s] == 0:
            visited[s] = 1
            # 인접 노드 탐색
        for w in abj_l[s]:
            if visited[w] == 0:
                my_stack.append(w)
                s = w
                break
        else:
            if my_stack:
                s = my_stack.pop()
                continue
            else:
                break

    if visited[e] == 1:
        return 1
    else:
        return 0

T = int(input())
for tc in range(1, T+1):
    # V = 노드의 수 / E = 간선의 수
    V, E = map(int, input().split())
    # 간선 정보를 받아와 바로 인접 리스트에 추가
    abj_l = [[] for _ in range(V+1)]
    for _ in range(E):
        f, t = map(int, input().split())
        # 화살 표가 있으므로 한 방향만 추가
        abj_l[f].append(t)

    # S = 출발 노드 / G = 도착 노드
    S, G = map(int, input().split())

    print(f'#{tc} {dfs(S, G, E)}')

