# 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

# 1차 시도
# 시작 시간 : 02/13 17:00
# 종료 시간 : 02/13 17:30 실패

# 2차 시도
# 시작 시간 : 02/15 11:00
# 종료 시간 : 02/15 12:00 실패

# 3차 시도
# 시작 시간 : 02/15 12:10
# 종료 시간 : 02/15 13:00 실패



import sys
# sys.stdin = open("5201_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    # 컨테이너 수  N 와 트럭 수 M
    N, M = map(int, input().split())
    # 컨테이너 무게
    ct = list(map(int, input().split()))
    # 트럭의 적재량
    truck = list(map(int, input().split()))

    # 트럭의 수와 컨테이너의 수를 비교하여 기준을 달리 해야함.
    # 트럭의 수가 많을 경우, 트럭을 기준으로 컨테이너를 순회하며 비교.
    # 컨테이너 수가 많을 경우, 컨테이너를 기준으로 트럭을 순회하며 비교.
    # 트럭의 적재량 컨테이너의 무게를 각 각 내림차순 정렬한다.

    ct.sort(reverse=True)
    truck.sort(reverse=True)

    # 옮겨진 화물의 전체 무게
    total_w = 0

    print(f'#{tc} {total_w}')

