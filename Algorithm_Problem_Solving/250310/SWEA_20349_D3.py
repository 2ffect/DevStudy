# 국민셔플

# 시작 시간 : 03/10 11:30
# 종료 시간 : 03/10 12:20

import sys
sys.stdin = open('20349_input.txt')

T = int(input())

for tc in range(1, T+1):
    # c : 카드의 수 / s : 셔플 set 시행 횟수
    c, s = map(int, input().split())
    # 카드 리스트
    card = [str(i) for i in range(1, c+1)]
    # 오버핸드 셔플을 진행해야 할 카드 장 수
    over_hand = int(c * 0.37)
    # 퍼펙트 셔플을 진행해야 할 카드의 장 수
    perfect = int(c * 0.5)

    new_card = []

    for _ in range(s):
        # 오버핸드 셔플 진행
        # 대상 리스트는 뒤집힌 상태여야 함
        over_hand_list = list(reversed(card))
        over_hand_card = []
        # 오버핸드 셔플 > over_hand의 수만큼 뒤에서 가져와, 앞으로 추가
        for i in range(over_hand-1, -1, -1):
            # 하나 가져오면
            over_hand_card.append(over_hand_list[i])
            # 리스트에서는 하나를 제거해준다.
            card.pop()
        # 오버핸드 셔플이 완료 된 카드 리스트
        after_over_hand = over_hand_card + card

        # 퍼펙트 셔플 진행
        # 대상 리스트 뒤집기
        before_perfect = list(reversed(after_over_hand))
        perfect_card = []
        # 퍼펙트 셔플 > perfect 수 만큼 가져와 번갈아 추가
        for j in range(perfect-1, -1, -1):
            # 하나 가져오면
            perfect_card.append(before_perfect[j])
            # 리스트에서는 하나를 제거해준다.
            after_over_hand.pop()

        new_card = []
        k = 0
        # 섞은 카드의 크기가 카드의 수와 같아지면 종료
        while len(new_card) != c:
            if k <= len(after_over_hand):
                new_card.append(after_over_hand[k])
            if k == len(perfect_card):
                continue
            else:
                new_card.append(perfect_card[k])

            k += 1

        # 셔플 1회 완료마다 각각의 카드를 갱신
        card = new_card
        new_card = new_card

    result = ' '.join(new_card)
    print(f'#{tc} {result}')