# Forth

# 시작 시간 : 02/20 21:00
# 종료 시간 : 02/20 21:48 성

# 피연산자는 스택에 쌓고, 연산자가 나오면 직전 스택 2개를 꺼내 연산을 한 뒤, 다시 쌓는다
# . 을 만나면 스택에 있는 값을 출력한다.

import sys
sys.stdin = open("4874_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    forth = input().split()

    my_stack = []

    for i in forth:
        if i not in '+-*/.%':
            my_stack.append(i)
            continue

        if i == '+':
            if len(my_stack) >= 2:
                b = int(my_stack.pop())
                a = int(my_stack.pop())
                my_stack.append(int(a + b))
            else:
                print(f'#{tc} error')
                break

        elif i == '-':
            if len(my_stack) >= 2:
                b = int(my_stack.pop())
                a = int(my_stack.pop())
                my_stack.append(int(a - b))
            else:
                print(f'#{tc} error')
                break

        elif i == '*':
            if len(my_stack) >= 2:
                b = int(my_stack.pop())
                a = int(my_stack.pop())
                my_stack.append(int(a * b))
            else:
                print(f'#{tc} error')
                break

        elif i == '/':
            if len(my_stack) >= 2:
                b = int(my_stack.pop())
                a = int(my_stack.pop())
                my_stack.append(int(a // b))
            else:
                print(f'#{tc} error')
                break

        elif i == '%':
            if len(my_stack) >= 2:
                b = int(my_stack.pop())
                a = int(my_stack.pop())
                my_stack.append(int(a % b))
            else:
                print(f'#{tc} error')
                break

        if i == '.':
            if len(my_stack) == 1:
                result = my_stack.pop()
                print(f'#{tc} {int(result)}')
            else:
                print(f'#{tc} error')