# 달팽이 숫자

# 1차 시도 - 제한 시간 70분
# 시작 시간 : 02/17 11:30
# 종료 시간 : 02/17 12:40 실패



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

    # 배열을 순회하면서 각 배열을 num_list로 바꿔줘야 함

    print(arr)