from collections import deque

# 연습문제

'''
input
7 8
4 2 1 2 1 3 5 2 4 6 5 6 6 7 3 7
'''

# s = 시작점, V = 마지막 정점의 번호
def bfs(s, V):
    # visited 생성 = 방문확인용
    # V 번 까지 인덱스를 가지기 때문에 V + 1
    visited = [0] * (V + 1)
    # deque 생성
    q = deque()
    # 시작점 인큐
    q.append(s)
    # 시작점 인큐 표시
    visited[s] = 1
    # 큐가 비워질 때 까지 반복 (큐가 empty가 아니면 계속 실행)
    while q:
        # 디큐해서 t에 저장
        t = q.popleft()
        # t 정점에 대한 처리 = 방문 순서를 출력,
        print(t)
        # t 에 인접한 정점 w 중, 인큐되지 않은 정점 탐색
        for w in adj_l[t]:
            if visited[w] == 0:
                # 인큐하고,
                q.append(w)
                # 인큐 표시를 할 때, 어떤 그룹으로 부터 추가가 되었는지 확인을 위해
                # visited[t] + 1로 함, 2번 그룹이면 1번 그룹으로 파생되므로 2 출력
                visited[w] = visited[t] + 1
    print(visited)

# 1번부터 V번 정점, E개의 간선
V, E = map(int, input().split())
arr = list(map(int, input().split()))

# 인접 리스트 만들기 (행 별로 가져오기)
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1) # 방향이 없는 경우 양쪽이기 때문에 추가

bfs(5, 7)
