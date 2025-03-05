# 학번 1346186

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    player = list(map(int, input().split()))
    # 정렬을 한 뒤
    player.sort()

    max_members = 0
    for i in range(N):
        # 기준 플레이어 선정
        main_player = player[i]
        members = 0
        for j in range(i, N):
            sub_player = player[j]
            if abs(main_player - sub_player) <= K:
                members += 1

        max_members = max(max_members, members)

    print(f'#{tc} {max_members}')