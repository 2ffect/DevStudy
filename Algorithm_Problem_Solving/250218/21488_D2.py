# 색칠하기
# 제한 시간 1시간

# 시작 시간 : 02/18 20:00
# 종료 시간 : 02/18 20:21

import sys
sys.stdin = open("21488_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    # 칠해야 할 배열을 만들어 10X10
    board = [list([0]*10) for _ in range(10)]
    # 칠할 영역의 수
    N = int(input())
    # 조건을 좌표의 범위와 색상으로 구분해서 받아온다.
    for _ in range(N):
        s1, s2, e1, e2, color = map(int, input().split())
        # 가져 온 범위를 활용해서 board에 칠한다. (색상을 더해준다)
        for i in range(s1, e1+1):
            for j in range(s2, e2+1):
                board[i][j] += color

    # board를 순회하며 값이 3 이상인 수를 센다.
    # 덧칠이 될 수 있으니까 3 이상이면 모두 보라색

    cnt = 0
    for k in range(10):
        for p in range(10):
            if board[k][p] >= 3:
                cnt += 1

    print(f'#{tc} {cnt}')