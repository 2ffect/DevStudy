# 농작물 수확하기

# 1차 시도
# 시작 시간 : 02/13 20:30
# 종료 시간 : 02/13 21:40 실패

# 2차 시도 - 코드 리셋
# 시작 시간 : 02/14 14:10
# 종료 시간 : 02/14 15:10 실패

# 3차 시도 - 코드 리셋
# 시작 시간 : 02/14 15:20
# 종료 시간 : 02/14 15:33 성공

import sys
sys.stdin = open("2805_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    total_value = 0


    # i 의 기준을 밖에서 정해두고
    # j 는 0 ~ N//2 만들어 각 각 [i][j]:[i][N-1-j] 슬라이싱으로 합계 계산
    # i 를 빼주며 다 합산
    # 이후 i를 더해주며 다 합산
    # 중복된 가운데 줄 값 빼주기
    i = N//2

    # 절반 중 위
    for j in range((N//2)+1):
        if i >= 0:
            total_value += sum(arr[i][j:N-j])
            i -= 1

    i = N//2

    # 절반 중 아래
    for j in range((N//2)+1):
        if i < N:
            total_value += sum(arr[i][j:N-j])
            i += 1

    i = N//2

    # 두 번 더해진 가운데 행의 합 빼주기
    result = total_value - sum(arr[i])

    print(f'#{tc} {result}')