import sys
sys.stdin = open("1961_input.txt", "r")

T = int(input())

for tc in range(1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 결과를 받을 빈 리스트 N*N 크기
    result = [[''] * N for _ in range(N*N)]

    # 시계방향 90도
    result_90 = list(zip(*arr[::-1]))
    # 시계방향 180도
    result_180 = list(zip(*result_90[::-1]))
    # 시계방향 270도
    result_270 = list(zip(*result_180[::-1]))

    result_90 = ''.join(list(map(str, result_90)))
