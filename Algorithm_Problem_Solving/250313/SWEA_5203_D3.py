# 베이비진 (그리디)

import sys
sys.stdin = open('5203_input.txt')

T = int(input())

for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    player_1 = []
    player_2 = []
    # 카드를 순회하며 하나씩 가져가면서 3장이 됐을 때 부터, triplet, run을 비교한다.
    # 먼저 나오면 승리 후 종료
    # 승부가 나지 않는다면 0을 출력
    # 승자
    winner = 0


    for i in range(12):
        # 짝수는 1번 플레이어에게
        if i % 2 == 0:
            player_1.append(cards[i])
            player_1 = sorted(player_1)
            player_1_set = list(set(player_1))

            # 트리플 검증
            for j in range(len(player_1) - 2):
                a, b, c = player_1[j], player_1[j + 1], player_1[j + 2]
                if a == b == c:
                    winner = 1
                    break

            # 런 검증
            for j in range(len(player_1_set) - 2):
                a, b, c = player_1_set[j], player_1_set[j + 1], player_1_set[j + 2]
                if a == (b - 1) == (c - 2):
                    winner = 1
                    break

            if winner:
                break

        # 홀수는 2번 플레이어에게
        if i % 2 != 0:
            player_2.append(cards[i])
            player_2 = sorted(player_2)
            player_2_set = list(set(player_2))

            # 트리플 검증
            for j in range(len(player_1) - 2):
                a, b, c = player_2[j], player_2[j + 1], player_2[j + 2]
                if a == b == c:
                    winner = 2
                    break

            # 런 검증
            for j in range(len(player_2_set) - 2):
                a, b, c = player_2_set[j], player_2_set[j + 1], player_2_set[j + 2]
                if a == (b - 1) == (c - 2):
                    winner = 2
                    break

            if winner:
                break

    print(f'#{tc} {winner}')
