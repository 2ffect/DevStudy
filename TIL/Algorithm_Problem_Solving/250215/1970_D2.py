# 쉬운 거스름돈 - 제한시간 2시간

# 1차 시도
# 시작 시간 : 02/15 14:30
# 종료 시간 : 02/15 15:04 성공

import sys
sys.stdin = open("1970_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    money = int(input())

    # 잔돈 리스트
    change = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    # 카운트
    counts = [0, 0, 0, 0, 0, 0, 0, 0]
    # 잔돈 리스트 크기
    N = len(change)

    # 돈이 0보다 많으면
    if money > 0:
        # 잔돈을 순회한다
        for i in range(N):
            # 남은 돈이 잔돈보다 커질 때 까지 계속
            while money >= change[i]:
                # 돈에서 잔돈을 빼면서 잔돈 위치의 인덱스에 +1
                money -= change[i]
                counts[i] += 1

    print(f'#{tc}')
    print(*counts)