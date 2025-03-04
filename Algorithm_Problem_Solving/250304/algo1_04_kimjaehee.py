# 깃발 게임 결승전

T = int(input())

for tc in range(1, T+1):
    # N = 팀원의 수 / M = 명령 횟수
    N, M = map(int, input().split())
    # 팀원의 초기 상태
    team = list(map(int, input().split()))
    # 명령
    orders = [list(map(int, input().split())) for _ in range(M)]


    # 명령을 하나씩 꺼내와서 수행
    for order in orders:
        start = order[1]
        order_range = order[2]
        for i in range(N):
            if i+1 == start:
                # 명령 수행 포인트와 i의 값이 같을때 idx = i 가 팀의 명령수행 기준점
                # 기준점에서 k 범위만큼 수행 k는 명령의 마지막 요소 나를 제외하고 비교를 진행
                # 범위가 유효할 때만,
                for j in range(1, order_range+1):
                    plus_i = i+j
                    minus_i = i-j
                    # 유효 할 때
                    if (0 <= plus_i < N) and (0 <= minus_i < N):
                        # 둘의 상태가 다른 경우
                        if team[plus_i] != team[minus_i]:
                            # 다음 명령 범위 탐색
                            continue

                        # 둘 다 1인 상태면, 반대로 변경
                        elif team[plus_i] == team[minus_i] == 1:
                            team[plus_i] = team[minus_i] = 0
                        # 둘 다 0인 상태면, 반대로 변경
                        elif team[plus_i] == team[minus_i] == 0:
                            team[plus_i] = team[minus_i] = 1

    print(f'#{tc}', " ".join(map(str, team)))