# Stack 1 - 연습문제 2. 괄호 검사

import sys
sys.stdin = open("21619_input.txt", "r")

T = int(input())

for tc in range(1, 1+T):
    txt = input()

    n = len(txt)
    top = -1
    stack = [0] * n

    # 짝이 맞게 잘 들어가 있다고 가정,
    result = 1

    # txt 에서 x를 순회하며
    for x in txt:
        # x 가 여는괄호면 스택에 push
        if x in '({[<':
            top += 1
            stack[top] = x

        # x 가 닫는 괄호면
        elif x in ')}]>':
            # 스택이 비어있는지 확인, 비어있는 경우 결과를 -1로 바꾼 뒤 검사 종료
            if top == -1:
                result = -1
                break

            # 스택에 존재하는 경우, 짝이 맞는 경우, 괄호를 하나 pop.
            else:
                top -= 1

    # txt를 다 순회 했는데 스택에 괄호가 남아있으면 == 짝이 안맞는 경우. 결과는 -1
    if top != -1:
        result = -1

    # 모두 짝이 잘 맞게 들어갔으면 1, 아니라면 -1을 결과값으로 받아 출력
    print(f'#{tc} {result}')