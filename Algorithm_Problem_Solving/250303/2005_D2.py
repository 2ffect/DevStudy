# 파스칼의 삼각형

# 시작 시간 : 03/03 10:58
# 종료 시간 : 03/03 11:40

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 숫자를 삽입 할 틀
    pascals = [[] for _ in range(N)]
    # 첫 열의 숫자는 1
    pascals[0].append(1)

    # 2번째 열 부터 삽입
    for i in range(1, N):
        # 스택 생성 - 스택은 항상 직전의 열을 그대로 가져온다.
        my_stack = pascals[i-1][:]
        # 2번째 열의 첫번째 숫자 넣기.
        pascals[i].append(1)
        # 두번째 숫자 부터 1~i 번까지 넣는다 0번째는 이미 삽입 함.
        # 직전 열의 마지막 숫자를 팝 한 뒤, 가장 마지막 숫자를 더해 삽입해준다.
        # 마지막에 1을 넣어준다.
        for j in range(1, i):
            pascals[i].append(my_stack.pop() + my_stack[-1])
        pascals[i].append(1)

    print(f'#{tc}')
    for pascal in pascals:
        print(*pascal)