# [0, 1, 2] 3개의 카드가 존재
# 2개를 뽑을 예정
# 중복 순열 코드

# 뽑은 카드를 저장
path = []
# 숫자 사용 여부를 기록
used = [False] * 7

# 숫자 범위가 매우 큰 경우
# dict, set 등의 자료구조로 해결

# cnt = 재귀 호출마다 누적되어 전달되어야 하는 값. (매개변수로 사용)
def recur(cnt):
    # 카드를 2개 뽑으면 종료
    if cnt == 3:
        # 종료 시 해야할 로직들을 작성
        print(*path)
        return

    # # 1. 1개의 카드를 뽑는다.
    # for num in range(1, 7):
    #     path.append(num)
    #     # 다음 재귀 호출
    #     recur(cnt + 1)
    #     # 맨 마지막꺼 하나 뺀다.
    #     path.pop()

    # 1. 1개의 카드를 뽑는다.
    for num in range(1, 7):
        # 이미 num을 봅았다면 뽑지마라.
        # == num을 뽑지 않았을 때 뽑아라.
        if used[num] is True:
            continue

        used[num] = True
        path.append(num)
        # 다음 재귀 호출
        recur(cnt + 1)
        # 맨 마지막꺼 하나 뺀다.
        path.pop()
        used[num] = False


# 처음 호출 할 때 시점이므로 초기값을 전달하여 시작
recur(0)