# 4866. [파이썬 S/W 문제해결 기본] 4일차 - 괄호검사

import sys
sys.stdin = open("4866_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    txt = input()

    # 스택 기본설정
    n = len(txt)
    top = -1
    stack = [0] * (n+1)

    # 정상인 상태라고 가정
    result = 1
    box = ''
    # txt 순회 하면서
    for x in txt:
        # x 가 여는 괄호일 경우 스택에 push
        if x in '({[<':
            top += 1
            stack[top] = x


        # x 가 닫는 괄호일 경우
        elif x in ')}]>':
            # 빈 스택이면 0
            if top == -1:
                result = 0
                break

            # x 값에 따라 top+1 을 비교, 다르면 result = 0 break
            if x == ')':
                if stack[top] != '(':
                    result = 0
                    break
            if x == '}':
                if stack[top] != '{':
                    result = 0
                    break
            if x == ']':
                if stack[top] != '[':
                    result = 0
                    break
            if x == '>':
                if stack[top] != '<':
                    result = 0
                    break

            else:
                top -= 1


    # 순회를 했는데 스택이 남은경우 비정상
    if top != -1:
        result = 0

    print(f'#{tc} {result}')
