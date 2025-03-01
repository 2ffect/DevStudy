# 행렬찾기

# 시작 시간 : 03/01 10:00
# 종료 시간 : 03/01 11:11

import sys
sys.stdin = open("1258_input.txt")

T = int(input())
for tc in range(1, T+1):
    # 창고의 크기
    N = int(input())
    # 창고 받아오기
    container = [list(map(int, input().split())) for _ in range(N)]
    # 화학물질 용기 세로 가로 길이를 담을 리스트
    subsets = []

    # 0이 아닌 정수의 좌표를 찾기 == 시작점
    for i in range(N):
        for j in range(N):
            if container[i][j] != 0:

                # 시작점의 좌표를 저장
                r, c = i, j

                # 시작점을 기준으로 행, 열 의 길이 측정 == 0 을 만날 때 까지의 크기를 기록

                # r을 갱신하며 행 길이 탐색
                col_len = 0
                for k in range(r, N):
                    # 0이 아닌 정수인 경우 길이를 추가
                    if container[k][c] != 0:
                        col_len += 1
                    # 0을 만나면 탈출
                    else:
                        break

                # c를 갱신하며 열 길이 탐색
                row_len = 0
                for p in range(c, N):
                    if container[r][p] != 0:
                        row_len += 1
                    else:
                        break

                # 용기 크기를 리스트에 추가
                subsets.append([col_len * row_len, col_len, row_len])

                # 용기 크기만큼 0으로 변경하기 == 탐색 완료처리
                for n in range(col_len):
                    for m in range(row_len):
                        container[i+n][j+m] = 0

    # 컨테이너 조사가 끝난 경우, 넓이가 작은 순서대로 담기. 넓이가 같으면 행이 작은 순서,,
    ans_len = len(subsets)
    subsets.sort()

    ans = []
    for subset in subsets:
        subset.pop(0)
        for num in subset:
            ans.append(num)

    print(f'#{tc} {ans_len}', *ans)
