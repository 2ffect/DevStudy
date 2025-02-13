# 1차 시도
# 시작 시간 : 2/12 17:00
# 종료 시간 : 2/12 17:21 실패.

# 2차 시도 (이어서)
# 시작 시간 : 2/12 20:00
# 종료 시간 : 2/12 20:22
# 성수린의 도움으로 성공

# 3차 시도


import sys
sys.stdin = open("1215_input.txt", 'r')

for tc in range(1, 11):
    n = int(input())
    arr = [list(input()) for _ in range(8)]

    # 찾아야 하는 회문의 길이 = n
    # 행, 열의 길이는 8로 고정
    # 행과 열을 모두 각 각 순회하며 회문을 찾은 뒤 cnt에 추가하기.
    # 각 각 행 열의 순회 조건은 8-n+1 까지
    # 회문의 조건에 맞는다면 cnt += 1

    cnt = 0
    # 행 순회하며 회문 찾기
    for i in range(8):
        for j in range(8-n+1):
            # 회문 범위를 가져와서, 회문이 맞는지 비교.
            for k in range(n):
                # 회문 조건에 안 맞으면 종료하고 i 구간 이동. break 사용.
                if arr[i][j+k] != arr[i][j+n-1-k]:
                    break

            # 회문이면 cnt +1
            else:
                cnt += 1

    # 열 순회하며 회문 찾기
    # 행 기준의 arr 를 시계 방향으로 90도 회전하면 열이 행이 됨
    arr_2 = list(zip(*arr[::-1]))

    for i in range(8):
        for j in range(8-n+1):
            # 회문 범위를 가져와서, 회문이 맞는지 비교.
            for k in range(n):
                # 회문 조건에 안 맞으면 종료하고 i 구간 이동. break 사용.
                if arr_2[i][j+k] != arr_2[i][j+n-1-k]:
                    break

            # 회문이면 cnt +1
            else:
                cnt += 1

    print(f'#{tc} {cnt}')