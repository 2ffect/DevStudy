# 오목 판정

# 1차 시도
# 시작 시간 : 02/14 15:40
# 종료 시간 : 02/14 16:40 실패

# 2차 시도 - 코드 리셋
# 시작 시간 : 02/14 16:50
# 종료 시간 : 02/14 17:38 성공


import sys
sys.stdin = open("11315_input.txt", "r")


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    # 오목이 없다고 가정
    result = 'NO'

    di = [0, 1, 1, 1, 0, -1, -1, -1]
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    for i in range(N):
        for j in range(N):
            # 돌이 있는 위치만 시행 돌이 아니면 break
            # 연속한 돌의 수 만큼 cnt +1, cnt가 5 이상이면 result = 'YES'
            if arr[i][j] == 'o':
                # 거기 돌이 있으면 몇 방향을 더 볼건데? 내 기준 최대 8방향을 봐야지. 상하좌우, 각각 대각까지
                for d in range(8):
                    # 각 방향으로 몇 칸을 더 갈건데 ? 나 빼고 5 만큼 더 가
                    # 방향을 바꿀 때 마다 cnt를 초기화 해줘야해
                    cnt = 0
                    for c in range(5):
                        ni = i + (di[d] * c)
                        nj = j + (dj[d] * c)
                        # 유효한지 확인부터 해보자
                        if (0 <= ni < N) and (0 <= nj <N):
                            # 유효 할 때 한 칸 이동한 위치가 돌이야 ?
                            if arr[ni][nj] == 'o':
                                # 그럼 횟수를 더해줘
                                cnt += 1
                                # 그러다 cnt가 5 이상이 되면 result 를 'YES'로 바꾸고 탈출해 더 볼 필요 없어 이미 오목이야
                                if cnt >= 5:
                                    result = 'YES'
                                    break
                            # 유효 할 때 한 칸왔는데 돌이 아니야? 그럼 브레이크.
                            else:
                                break

    print(f'#{tc} {result}')