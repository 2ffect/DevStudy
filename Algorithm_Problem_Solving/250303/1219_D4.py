# 길찾기

# 시작 시간 : 03/03 18:46
# 종료 시간 : 03/03 19:13

# 시작점 0 / 도착점 99
import sys
sys.stdin = open("1219_input.txt")

# s = 출발점 / e = 도착점
def dfs(s, e):
    visited = [0] * (N+1)
    my_stack = []

    while True:
        # 방문 기록
        if visited[s] == 0:
            visited[s] = 1

        for w in adj_l[s]:
            if visited[w] == 0:
                visited[w] = 1
                my_stack.append(w)
                s = w
                break

        else:
            if my_stack:
                s = my_stack.pop()
                continue
            else:
                break

    if visited[e] != 0:
        return 1
    else:
        return 0

for _ in range(10):
    # tc와 간선의 수:
    tc, E = map(int, input().split())
    # 순서 쌍 받아오기
    num = list(map(int, input().split()))
    # 도착지
    N = 99
    # 인접 리스트 생성
    adj_l = [[] for _ in range(N+1)]
    # 인접 리스트에 추가
    for i in range(E):
        f, t = num[i*2], num[i*2+1]
        adj_l[f].append(t)

    print(f'#{tc} {dfs(0, 99)}')