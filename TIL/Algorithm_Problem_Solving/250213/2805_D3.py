# 농작물 수확하기

# 1차 시도
# 시작 시간 : 02/13 20:30
# 종료 시간 : 02/13 21:40 실패

# 2차 시도
# 시작 시간 : 02/14 12:00
# 종료 시간 : 02/14 12:45

import sys
sys.stdin = open("2805_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    total_value = 0

    i = N//2
    # 행을 한 줄 씩 가져와서 더한다.
    # N//2 를 기준으로 가져오면 정 가운데 행을 가져오니까
    for j in rnage(N):


    print(f'#{tc} {total_value}')