# [파이썬 S/W 문제해결 구현] 2일차 - 최소합 (완전탐색)

import sys
sys.stdin = open('5188_input.txt')

def dfs(N, arr):
    global min_sum
    # 스택 생성, 초기값 푸시
    my_stack = [[0, 0, arr[0][0]]]

    # 스택이 텅텅 빌 때 까지
    while my_stack:
        # 팝 하여 가져오기
        pi, pj, num_sum = my_stack.pop()
        # 가져온 위치가 맨 오른쪽 아래라면
        if (pi == N-1) and (pj == N-1):
            # 최소값 비교 후 갱신
            min_sum = min(min_sum, num_sum)
            # 브레이크를 하면 끝까지 온 경우 한번만 조회함,
            # 컨티뉴로 스택이 빌 때 까지 계속 확인하고 갱신해줘
            continue

        # 아니면, 오른쪽이나 아래쪽으로 진행
        for di, dj in [[0, 1], [1, 0]]:
            ni, nj = pi + di, pj + dj
            # 유효하면
            if (0 <= ni < N) and (0 <= nj <N):
                # 스택에 담기
                # 유효한 좌표와, 현재 좌표까지의 합 + 유효한 좌표의 값 == 누적합
                my_stack.append([ni, nj, num_sum + arr[ni][nj]])

    # 갱신한 최소값을 반환
    return min_sum


T = int(input())

for tc in range(1, T+1):
    # 배열의 크기 N
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 99999999

    print(f'#{tc} {dfs(N, arr)}')