# 연속 3장의 트럼프 카드
card = ['A', 'J', 'Q', 'K']
path = []
result = 0

def count_three():
    if path[0] == path[1] == path[2]: return True
    if path[1] == path[2] == path[3]: return True
    if path[2] == path[3] == path[4]: return True
    return False

def recur(cnt):
    global result
    # 카드 5장을 뽑으면 종료
    if cnt == 5:
        # 5장 뽑았을 때 연속 된 3개가 나오면 counting
        if count_three():
            result += 1
        return

    for idx in range(4):
        path.append(card[idx])
        recur(cnt + 1)
        path.pop()


recur(0)
print(result)