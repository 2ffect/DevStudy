# [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크
# 제한 시간 : 2 시간

# 1차 시도
# 시작 시간 : 02/15 16:00
# 종료 시간 : 02/15 18:00 실패

# 2차 시도
# 시작 시간 :
# 종료 시간 :

import sys
sys.stdin = open("23490_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_work = 0

    arr.sort(key=lambda x: (x[1], x[0]))
    print(arr)