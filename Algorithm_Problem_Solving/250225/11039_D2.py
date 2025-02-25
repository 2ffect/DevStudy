# 사각형 찾기

# 시작 시간 : 14:40
# 종료 시간 : 15:16 성공

# N*N 의 배열을 입력 받는다.
# 기준점으로 부터 연속된 1의 가로와 세로 수를 구해 둘을 곱한 값 중 최고 높은 값을 찾는다.
# cnt는 1부터 시작.

import sys
sys.stdin = open("11039_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]


    max_multipli = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:

                # arr[i][j]가 1일 경우의 좌표를 저장
                new_i = i
                new_j = j

                # 열 개수 카운팅
                row_cnt = 0
                for p in range(j, N):
                    # 기준점 i를 두고 p만 변경하며 행 검사, 1이면 카운트 1 추가.
                    if arr[new_i][p] == 1:
                        row_cnt += 1
                    # 1이 아닌경우 브레이크
                    else:
                        break

                # 행 개수 카운팅
                column_cnt = 0
                for p in range(i, N):
                    # 기준점 j를 두고 p만 변경하며 열 검사, 1이면 카운트 1 추가.
                    if arr[p][new_j] == 1:
                        column_cnt +=1
                    # 1이 아닌경우 브레이크
                    else:
                        break

                # 곱하기
                multipli = (row_cnt * column_cnt)

                # 최대값 갱신
                if multipli >= max_multipli:
                    max_multipli = multipli


    print(f'#{tc} {max_multipli}')