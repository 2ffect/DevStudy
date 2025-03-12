
def KFC(num):
    # 종료 조건
    if num == 5:
        return

    # 재귀 호출 전 들어가야 할 로직
    print(num)

    # 다음 재귀 호출 (매개변수를 변경하여 전달)
    KFC(num + 1)

    # 돌아오면서 애야 할 로직직
    print(num)

KFC(0)
print('끝')