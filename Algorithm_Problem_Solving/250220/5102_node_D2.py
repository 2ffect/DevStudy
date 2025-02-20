# 노드의 거리

# 1차 시도
# 시작 시간 : 02/20 11:53
# 종료 시간 : 02/20 12:46 실패

# 2차 시도
# 시작 시간 : 02/20 14:00
# 종료 시간 : 02/20 14:12 성공

# V 개의 노드와 방향성이 없는 E개의 간선이 주어진다.
# 출발 노드와 도착 노드가 주어질 때 몇 개의 간선을 거쳐야 하는지 출력.
# 노드는 1번부터 존재, 연결되지 않았을 수 있음
# 주어진 인접 정보를 바탕으로 방문기록을 모두 생성하여 출발점과 도착점으로의 떨어진 거리만큼의 그룹을 나눠준다.
# 출발 노드와 도착노드의 정보를 받아, 노드간의 거리를 리턴한다.
# 출발 노드와 도착노드가 이어지지 않는다면 0을 리턴한다.

from collections import deque
import sys
sys.stdin = open("5102_input.txt", "r")

# S 출발 노드, G 도착 노드, V 마지막 노드
def bfs(S, G, V):
    # 방문 기록
    visited = [0] * (V + 1)
    # 큐 생성
    q = deque()
    # 인큐
    q.append(S)
    # 인큐 표시
    visited[S] = 1
    # 큐가 비워질 때 까지 반복
    while q:
        # 디큐해서 t에 저장
        t = q.popleft()
        # t 에 인접한 정점 w 중, 인큐되지 않은 정점 탐색
        for w in adj_l[t]:
            if visited[w] == 0:
                # 인큐하고,
                q.append(w)
                # 인큐 표시를 할 때, 어떤 그룹으로 부터 추가가 되었는지 확인을 위해
                # visited[t] + 1로 함, 2번 그룹이면 1번 그룹으로 파생되므로 2 출력
                visited[w] = visited[t] + 1

    if visited[S] - visited[G] == S:
        return 0

    return abs(visited[S] - visited[G])

T = int(input())

for tc in range(1, T+1):
    ### 인풋 받기
    # V = 노드 수  E = 간선 수
    V, E = map(int, input().split())
    # 인접 리스트 만들고
    adj_l = [[] for _ in range(V+1)]
    # 인풋을 E 만큼 받아서 인접 리스트에 추가하기
    for _ in range(E):
        f, s = map(int, input().split())
        adj_l[f].append(s)
        # 방향성이 없기 때문에 양 방향 넣어주기
        adj_l[s].append(f)
    # S = 출발 노드, G = 도착노드
    S, G = map(int, input().split())
    ### 인풋 끝

    # 첫 노드부터 마지막 노드까지 모두 탐색이 되어야한다.
    # 탐색 후 출발 노드부터 도착 노드까지 간선의 수를 리턴
    # bfs 의 변수로는 ?
    # 시작 노드, 도착 노드, 마지막 노드 ????????
    result = bfs(S, G, V)

    print(f"#{tc} {result}")