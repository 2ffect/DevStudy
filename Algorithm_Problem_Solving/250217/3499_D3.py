# 퍼펙트 셔플

# 1차 시도
# 시작 시간 : 02/17 17:15
# 종료 시간 : 02/17 17:34 성공

import sys
sys.stdin = open("3499_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    txt = input().split()

    card_1 = []
    card_2 = []

    new_card = []

    for i in range(N):
        if i < N/2:
            card_1.append(txt[i])
        if i >= N/2:
            card_2.append(txt[i])

    for j in range(N):
        if len(card_1) > j:
            new_card.append(card_1[j])
        if len(card_2) > j:
            new_card.append(card_2[j])

    result = ' '.join(new_card)

    print(f'#{tc} {result}')
