# 비밀번호

# 시작 시간 : 03/03 10:30
# 종료 시간 : 03/03 10:42

for tc in range(1, 11):
    r, code = input().split()

    my_stack = []

    for i in code:
        if len(my_stack) == 0:
            my_stack.append(i)
        elif i != my_stack[-1]:
            my_stack.append(i)
        elif i == my_stack[-1]:
            my_stack.pop()

    print(f'#{tc}', "".join(my_stack))
