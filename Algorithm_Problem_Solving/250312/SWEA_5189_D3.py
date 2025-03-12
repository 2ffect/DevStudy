# [파이썬 S/W 문제해결 구현] 2일차 - 전자카트 (완전탐색)

import sys
sys.stdin = open('5189_input.txt')

def battery(idx, sum_v):
    global min_v

    # 모든 곳을 방문한 경우 (출발지로 돌아온 경우)
    if 0 not in visited:
        # 최소 소비량 갱신
        min_v = min(min_v, sum_v)
        return

    # 방문 할 곳
    for j in range(N):
        # 현재위치는 방문하지 않는다.
        if j == idx:
            continue
        # 이미 방문한 곳은 방문하지 않는다.
        if visited[j] == 1:
            continue
        # j 가 0 인데(출발지로 가야하는데), 아직 방문하지 않은 곳이 있으면 방문하지 않는다.
        # visited[1:] == 1번 인덱스부터 끝까지 (출발지를 제외하고)
        if j == 0 and 0 in visited[1:]:
            continue

        # 방문표시
        visited[j] = 1
        # 현재 인덱스와 배터리 누적합
        battery(j, sum_v + in_arr[idx][j])
        # 방문표시 해제
        visited[j] = 0

    return min_v


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    in_arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    min_v = 99999999

    print(f'#{tc} {battery(0,0)}')