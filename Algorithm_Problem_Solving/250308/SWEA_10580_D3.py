# 전봇대

# 시작 시간 : 03/09 18:50
# 종료 시간 : 03/09 19:06

import sys
sys.stdin = open('10580_input.txt')

T = int(input())

for tc in range(1, T+1):
    # 전선의 수
    N = int(input())
    # 전선 리스트
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 겹친 전선의 수
    cnt = 0

    # 전선을 하나씩 가져와서 기준점으로 삼기
    for i in range(N):
        # 기준 전선의 시작점
        start = arr[i][0]
        # 기준 전선의 끝점
        end = arr[i][1]

        # 기준점 다음 전선부터, 끝 전선까지 비교
        for j in range(i + 1, N):
            # 비교대상 전선의 시작점 끝점
            a, b = arr[j][0], arr[j][1]

            # 비교대상 전선의 시작점이 기준 전선보다 낮으면서 끝점이 기준 전선의 끝점보다 높으면 겹친다.
            if (a < start) and (b > end):
                cnt += 1

            # 비교대상 전선의 시작점이 기준 전선보다 높으면서 끝점이 기준 전선의 끝점보다 낮으면 겹친다.
            elif (a > start) and (b < end):
                cnt += 1

    print(f'#{tc} {cnt}')