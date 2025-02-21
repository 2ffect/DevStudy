# contact

# 시작 시간 : 02/20 14:30
# 종료 시간 : 02/20 15:36 실패

# 시작 시간 : 02/21 15:50
# 종료 시간 :


# 비상연락을 돌리는데, 출발 노드로부터 연락할 수 있는 최대 노드까지 연락하였을 때,
# 마지막 노드 그룹에 속하는 숫자 중 가장 높은 숫자를 출력하면 된다.

# 노드의 방향이 정해져있기 때문에 단방향으로 인접리스트를 추가하고,
# bfs로 탐색하여 출발 노드부터 마지막 노드까지 순회한 뒤 마지막 그룹을 찾고
# 마지막 그룹에 속하는 노드들 중 가장 높은 숫자를 리턴 == 결과

import sys
# sys.stdin = open("1238_input.txt", "r")
from collections import deque

# bfs
# 시작점을 넣었을 때 갈 수 있는 모든 방문점을 방문한 뒤, 시작점과 가장 멀리 있는 그룹 내에서 가장 높은 숫자를 반환
def bfs(S, V):
    # 방문기록 생성
    visited = [0] * (V + 1)
    # 큐 생성
    q = deque()
    # 인큐
    q.append(S)
    # 방문 기록
    visited[S] = 1
    # 큐가 전부 빌 때 까지 방문
    while q:
        # 디큐
        t = q.popleft()
        # 인접한 w 탐색
        for w in adj_l[t]:
            # 방문한 적 없는 노드라면
            if visited[w] == 0:
                # 인큐
                q.append(w)
                # 방문 기록 - t로 부터 몇 번 떨어진 그룹인지.
                visited[w] = visited[t] + 1

    return visited

for tc in range(1):
    # L = 데이터 길이, S = 시작점 (비상 연락의 시작점!!!!!!)
    L, S = map(int, input().split())
    # 데이터 리스트
    data = list(map(int, input().split()))
    V = max(data)
    # 인접 리스트 생성
    adj_l = [[] for _ in range(V + 1)]

    # 데이터 쌍별로 인접 리스트에 넣기
    for i in range(L//2):
        fr, to = data[i * 2], data[i * 2 + 1]
        # 방향이 있기 때문에 from -> to 만 인접 리스트 추가
        adj_l[fr].append(to)

    # bfs
    result = bfs(S, V)

    # 값이 존재하는 최대 거리 노드의 그룹과 그룹의 인덱스 찾기
    max_group = []
    idx = []
    for i in range(V+1):
        if len(adj_l[i]) > 0:
            # 인접한 노드일 때
            if result[i] > 0:
                max_group.append(result[i])
                idx.append(i)

    # 최대 그룹 값을 가진 인덱스 찾기
    x = (max(max_group))
    max_idx = []
    for i in range(len(max_group)):
        if max_group[i] == x:
            max_idx.append(idx[i])

    # 최대 그룹 값을 가진 인접 리스트 인덱스를 활용해 하나의 리스트에 추가
    max_list = []
    print(max_idx)
    for i in range(V+1):
        if i in max_idx:
            for j in range(len(adj_l[i])):
                max_list.append(adj_l[i][j])

    # 추가 된 값 중 최대값을 찾아 출력
    print(f'#{tc} {max(max_list)}')