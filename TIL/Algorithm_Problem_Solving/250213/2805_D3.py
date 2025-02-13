# 농작물 수확하기

# 1차 시도
# 시작 시간 : 02/13 20:30
# 종료 시간 : 02/13 21:40 싪패

# 2차 시도

import sys
sys.stdin = open("2805_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    total_value = 0

    print(f'#{tc} {total_value}')