# 달팽이 숫자

# 1차 시도 - 제한 시간 70분
# 시작 시간 : 02/17 11:30
# 종료 시간 : 02/17 12:40 실패

# 2차 시도
# 시작 시간 :
# 종료 시간 :



import sys
# sys.stdin = open("1954_input.txt", "r")

T = int(input())

for tc in range(1):
    N = int(input())

    # N 크기의 배열에 들어 갈 숫자 리스트.
    num_list = []
    for i in range(1, (N*N)+1):
        num_list.append(i)
    # 숫자가 들어갈 배열을 생성
    arr = [list([0] * N) for _ in range(N)]

    # 4 방향으로 간다.
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    for i in range(N):
        for j in range(N):
