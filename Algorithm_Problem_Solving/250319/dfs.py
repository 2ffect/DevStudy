import sys
sys.stdin = open('graph.txt')

def dfs(v):
    # 보통 그래프 문제들에서
    # K개의 노드 방문했다면 종료
    # N 개를 모두 방문했다면 경로 출력 등등
    # if 종료 시 해야할 것들 or 가지치기:
    #     return

    print(v, end=' ')

    # 인접한 노드들을 모두 확인하면서 한 군데로 진행
    for next_v in graph[v]:
        if visited[next_v]:
            continue

        visited[next_v] = 1
        dfs(next_v)

N, M = map(int, input().split())
# 그래프 저장
# - 비어있는 그래프 생성
# - 그래프 정보를 입력받아 넣기
# 인접 행렬 (N * N 의 0 배열)
# graph = [[0] * N for _ in range(N + 1)]
# 인접 리스트 (N * N ([]))
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    # from / to
    f, t = map(int, input().split())
    graph[f].append(t)
    # 양 방향일 경우, 반대 방향의 경우도 저장해야 함
    graph[t].append(f)

# 방문 기록
visited = [0] * (N + 1)
# 방문기록 초기화
visited[1] = 1

dfs(1)