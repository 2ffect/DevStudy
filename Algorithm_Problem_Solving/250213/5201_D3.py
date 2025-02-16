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

# 제한 시간 2시간
# 4차 시도
# 시작 시간 : 02/16 15:55
# 종료 시간 : 02/16 17:16 성공

import sys
sys.stdin = open("5201_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    # 컨테이너 수  N 와 트럭 수 M
    N, M = map(int, input().split())
    # 컨테이너 무게
    ct = list(map(int, input().split()))
    # 트럭의 적재량
    truck = list(map(int, input().split()))

    # 맨 앞이 가장 큰 수
    ct.sort(reverse=True)
    truck.sort(reverse=True)

    # 최종 운반 무게
    total_w = 0
    # i 는 항상 0으로 고정
    i = 0
    # 최대 반복 횟수는 컨테이너와 트럭의 수를 비교해 더 많은 만큼
    max_try = max(N, M)

    for _ in range(max_try):
        # 트럭의 길이나 컨테이너의 길이가 0 이상 일 경우만 가장 첫 값을 비교해서 트럭이 크면 적재, 아니면 적재 불가
        if len(truck) != 0 and len(ct) != 0:
            if truck[i] >= ct[i]:
                total_w += ct[i]
                ct.pop(i)
                truck.pop(i)
            # 컨테이너가 더 크면 일단 컨테이너 제거, 다음 컨테이너 적재 가능성 있음.
            else:
                ct.pop(i)

        # 가장 큰 컨테이너 무게가 가장 큰 적재량보다 무거우면 적재 불가 break
        else:
            break

    print(f'#{tc} {total_w}')