# 반복문자 지우기

# 시작 시간 : 03/03 10:46
# 종료 시간 : 03/03 10:49

T = int(input())

for tc in range(1, T+1):
    code = input()

    my_stack = []

    for i in code:
        if len(my_stack) == 0:
            my_stack.append(i)
        elif i != my_stack[-1]:
            my_stack.append(i)
        elif i == my_stack[-1]:
            my_stack.pop()

    print(f'#{tc} {len(my_stack)}')