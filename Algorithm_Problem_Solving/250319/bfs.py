import sys
sys.stdin = open('graph.txt')

def bfs(v):
    q = [v] # 시작점을 넣은 상태로 출발

    while q:
        # 가장 앞에 있는 노드를 뽑는다.
        # 해당 노드가 갈 수 잇는 노드들을 queue에 넣는다.
        now = q.pop(0)
        print(now, end=' ')

        for next_v in graph[now]:
            if visited[next_v]:
                continue

            visited[next_v] = 1
            q.append(next_v)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    f, t = map(int, input().split())
    graph[f].append(t)
    graph[t].append(f)

visited[1] = 1
bfs(1)