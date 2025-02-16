# 스택 괄호검사 연습문제

txt = input()
top = -1
stack = [0] * 100

ans = 1                 # 짝이 맞다고 가정
for x in txt:
    if x == '(':        # 여는 괄호는 push,  if x in '({[<' 방식의 구현도 가능.
        top += 1
        stack[top] = x
    elif x == ')':       # 닫는 괄호는 pop
        if top == -1:   # 스택이 비어 있는 경우
            ans = 0     # 짝이 맞지 않아
            break       # for문 탈출
        else:
            top -= 1    # 소괄호만 있으므로 비교작업 생략 후 top -1

if top > -1:
    ans = 0

print(ans)