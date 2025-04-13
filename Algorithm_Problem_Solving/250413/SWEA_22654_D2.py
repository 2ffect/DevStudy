# 차윤이의 RC카
import sys
sys.stdin = open('22654_input.txt')
for tc in range(1, int(input()) + 1):
    # 맵 크기
    N = int(input())
    field = [input() for _ in range(N)]
    # 커맨드 수
    M = int(input())

    commands = []
    # 각 커맨드 별 인풋받아 명령어 목록에 추가
    for _ in range(M):
        i, command = input().split()
        commands.append([int(i), command])

    rc_car = (0, 0)
    # RC카 위치 찾기
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                rc_car = (i, j)

    # rc카가 바라보는 방향
    delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # 기본적으로 바라보는 방향은 북쪽
    d = 0
    # 명령어 R == d + 1
    # 명령어 L == d - 1

    # 명령어를 반복하며 field 탐색
    for i in range(M):
        j, command = commands[i]

