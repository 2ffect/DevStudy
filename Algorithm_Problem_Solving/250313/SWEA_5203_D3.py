# 베이비진 (그리디)

import sys
sys.stdin = open('5203_input.txt')

T = int(input())

for tc in range(1, T + 1):
    cards = list(map(int, input().split()))
    # card의 수
    N = 12

    player_1 = []
    player_2 = []
    # 카드를 순회하며 하나씩 가져가면서 3장이 됐을 때 부터, triplet, run을 비교한다.
    # 먼저 나오면 승리 후 종료
    # 승부가 나지 않는다면 0을 출력
    # 승자
    winner = 0


    for i in range(N):
        # 짝수는 1번 플레이어에게
        if i % 2 == 0:
            player_1.append(cards[i])
            if len(player_1) >= 3:
                count_num = [0] * 11

                for j in range(len(player_1)):
                    # 숫자 등록
                    count_num[player_1[j]] += 1

                for k in range(1, 10):
                    # 3보다 크거나 같으면 같은숫자가 3개 이상 트리플렛
                    if count_num[k] >= 3:
                        winner = 1
                        break

                for p in range(1, 9):
                    a, b, c = count_num[p], count_num[p + 1], count_num[p + 2]
                    if a == (b - 1) == (c - 2):
                        winner = 1
                        break

        if winner != 0:
            break

        # 홀수는 2번 플레이어에게
        if i % 2 != 0:
            player_2.append(cards[i])
            if len(player_2) >= 3:
                count_num_2 = [0] * 11

                for j in range(len(player_2)):
                    # 숫자 등록
                    count_num_2[player_2[j]] += 1

                for k in range(1, 10):
                    # 3보다 크거나 같으면 같은숫자가 3개 이상 트리플렛
                    if count_num_2[k] >= 3:
                        winner = 1
                        break
                for p in range(1, 9):
                    a, b, c = count_num_2[p], count_num_2[p + 1], count_num_2[p + 2]
                    if a == (b - 1) == (c - 2):
                        winner = 1
                        break

        if winner != 0:
            break

    print(f'#{tc} {winner}')
