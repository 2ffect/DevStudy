# stack 연습문제 1
# 3개의 데이터를 스택에 저장하고 다시 3번 꺼내기

top = -1
stack = [0] * 10

# push 3번 하기
top += 1        # top : -1 > 0 으로 이동
stack[top] = 1  # stack[0] 에 1을 저장
                # psuh(1)의 역할을 수행
top += 1        # push(2)
stack[top] = 2
top += 1        # push(3)
stack[top] = 3
print(stack)    # [1, 2, 3, 0, 0, 0, 0, 0, 0, 0]

# pop 3번 하기
top -= 1                # top : 2 > 1 으로 이동
print(stack[top+1])     # 3 stack[1+1] 에 저장 된 3을 호출
                        # pop() 역할을 수행
top -= 1
print(stack[top+1])     # 2
top -= 1
print(stack[top+1])     # 1