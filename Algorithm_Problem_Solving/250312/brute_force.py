#주사위 3개를 던저 합이 10 이하인 경우는 몇개인가?

path = []
result = 0

def dice_sum(cnt, total):
    global result
    # 이미 10을 넘으면 더 이상 볼 필요가 없다.
    # 기저 조건에서 경우의 수를 많이 줄여주는 기법
    if total > 10:
        return

    if cnt == 3:
        if total <= 10:
            result += 1
        return

    for num in range(1, 7):
        path.append(num)
        dice_sum(num + 1, total + num)
        path.pop()


dice_sum(0, 0)
print(result)