# DFS 연습문제
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(v, N):                  # v 출발 정점 ,  N 마지막정점
    visited = [0] * (N + 1)     # 방문 표시 리스트
    stack = []                  # 스택

    while True:
        if visited[v] == 0:     # 첫 방문이라면,
            visited[v] = 1      # 방문 표시를 해
            print(v)            # 첫 방문임을 알리기

        for w in adj_list[v]:   # v에 인접하고 방문하지 않은 w가 있다면
            if visited[w] == 0:
                stack.append(v) # 현재 정점을 stack에 push
                v = w           # w로 이동
                break
        else:                   # 더 이상 갈 곳이 없는 경우
            if stack:
                v = stack.pop() # pop
            else:
                break



V, E = map(int, input().split())
graph = list(map(int, input().split()))

# 인접 리스트 만들기
# 빈 리스트로 생성 한 뒤, 인접 된 graph 값을 각 v 별 인덱스에 삽입?
adj_list = [[] for _ in range(V+1)]

for i in range(E):
    v, w = graph[i*2], graph[i*2+1]

    adj_list.append(v)