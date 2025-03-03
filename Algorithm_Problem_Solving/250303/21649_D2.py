# 연습문제 3. 그래프 탐색

# v = 출발 정점, N 마지막 정점
def dfs(v, N):
    # 방문 리스트 (최대 정점의 +1)
    visited = [0] * (V+1)
    # 스택 생성
    my_stack = []
    # 결과
    result = []

    while True:
        # 방문을 안 한 정점이라면 방문 기록
        if visited[v] == 0:
            visited[v] = 1
            # 방문 순서를 result에 추가하기
            result.append(str(v))
        # 현재 정점을 기준으로 방문하지 않은 인접 정점 찾기
        for w in abj_l[v]:
            # 방문하지 않았다
            if visited[w] == 0:
                # 현재 위치를 스택에 저장
                my_stack.append(v)
                # 현재 위치를 해당 정점으로 옮긴 뒤 for문 탈출
                v = w
                # break for w
                break

        # 모든 정점을 방문 했다면, 스택을 하나씩 빼며 재확인
        else:
            if my_stack:
                v = my_stack.pop()
                continue
            # 스택이 전부 비었다면 while 탈출
            else:
                # break for while
                break

    return '-'.join(result)

# V = 정점의 개수, E = 간선의 개수
V, E = map(int, input().split())
# 그래프
graph = list(map(int, input().split()))
# 인접 리스트 만들기 정점의 수 += 1
abj_l = [[] for _ in range(V+1)]

# 인접 리스트에 담기
for i in range(E):
    w, p = graph[i * 2], graph[(i * 2) + 1]
    # 방향이 없기 때문에 양방향으로 담기
    abj_l[w].append(p)
    abj_l[p].append(w)

print(f'#1 {dfs(1, V)}')