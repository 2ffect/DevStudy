# 공 굴리기

# 시작 시간 : 03/02 15:30
# 종료 시간 : 03/02 16:43 성공

# 공이 굴러갈 수 있는 최장 경로의 길이 찾기.
# 현재 위치에서 4방향을 돌러본 뒤 가장 낮은 숫자로 이동한다.
# 더 이상 굴러갈 곳이 없다면 종료한다.
# 모든 배열의 요소를 탐색 한 뒤 최장으로 갈 수 있는 길이를 찾는다 ?

import sys
sys.stdin = open("IM_1_input.txt")

T = int(input())

for tc in range(1, T+1):
    # 주어지는 배열의 크기
    N = int(input())
    # 배열
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 공이 굴러간 거리 중 가장 긴 거리
    max_len = 0

    # 탐색 방향
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 기준점 지정 / 모든 배열에서 조회 해야함
    for i in range(N):
        for j in range(N):

            # 출발점 초기화
            k, p = i, j
            # 현재 출발점에서 공이 굴러간 거리
            p_len = 1

            # 더 이상 갈 수 없을 때 까지 진행
            while True:
                num_list = []
                for d in range(4):
                    nk = k + di[d]
                    np = p + dj[d]

                    # 이동할 좌표가 유효하면서 현재 위치보다 작을경우 리스트에 추가
                    if (0 <= nk < N) and (0 <= np < N) and arr[k][p] > arr[nk][np]:
                        # 해당 숫자와 좌표를 모두 저장
                        num_list.append([arr[nk][np], nk, np])

                # 추가된 좌표가 있다면
                if len(num_list) >= 1:
                    num_list.sort()
                    # 가장 낮은 숫자로 좌표 이동 후 길이 추가 후 이동
                    k, p = num_list[0][1], num_list[0][2]
                    p_len += 1
                    continue

                # 추가 할 좌표가 없다면 건너뛰기
                else:
                    max_len = max(max_len, p_len)
                    break


    print(f'#{tc} {max_len}')