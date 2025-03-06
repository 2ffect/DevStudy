# 사칙 연산

import sys
sys.stdin = open("1232_input.txt")

# 후위 순회
def post_order(v):
    global my_stack
    if v:
        post_order(left[v])
        post_order(right[v])

        if my_stack:
            if num[v] == '-':
                a = my_stack.pop()
                b = my_stack.pop()
                my_stack.append(a - b)
            elif num[v] == '+':
                a = my_stack.pop()
                b = my_stack.pop()
                my_stack.append(a + b)
            elif num[v] == '/':
                a = my_stack.pop()
                b = my_stack.pop()
                my_stack.append(int(a // b))
            elif num[v] == '*':
                a = my_stack.pop()
                b = my_stack.pop()
                my_stack.append(int(a * b))

        else:
            my_stack.append(num[v])

    return my_stack

for tc in range(1):
    # 정점의 수
    N = int(input())
    # 간선의 수
    E = N - 1

    left = [0] * (N + 1)
    right = [0] * (N + 1)
    par = [0] * (N + 1)
    num = [0] * (N + 1)

    for _ in range(N):
        in_put = input().split()
        # 연산자 확인
        check = in_put[1]
        # 연산자라면 자식이 존재.
        if check in '-+/*':
            # 기준 정점
            n = int(in_put[0])
            num[n] = check

            # 왼쪽 노드가 비었으면 삽입
            if left[n] == 0:
                left[n] = int(in_put[2])
                par[int(in_put[2])] = n
                right[n] = int(in_put[3])
                par[int(in_put[3])] = n
        # 연산자가 아니라면 리프노드
        else:
            n = int(in_put[0])
            num[n] = int(in_put[1])

    root = 1
    for i in range(1, N+1):
        if par[i] == 0:
            root = i
            break

    my_stack = []
    post_order(root)