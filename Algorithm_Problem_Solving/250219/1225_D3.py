# 암호생성기

# 시작 시간 : 02/19 16:00
# 종료 시간 : 02/19 16:54 성공
from collections import deque

import sys
sys.stdin = open("1225_input.txt", "r")

# 8자리 숫자를 받아온다.
# 맨 앞문자를 -1 부터 -5까지 순서대로 한 뒤 맨 뒤로 보내는 과정을 반복한다.
# 빼기를 한 결과값이 0이 되거나, 0보다 작을 경우 0으로 저장하고 그만둔다
# 그 때 까지의 값을 출력하면 비밀번호가 된다.

T = 10
for i in range(1, T + 1):
    tc = int(input())
    password = deque(map(int, input().split()))

    # password 안에 0이 생길 때 까지 반복
    while 0 not in password:
        # 1 부터 5까지가 1 사이클 사이클은 반복수행
        for i in range(1, 6):
            # 가장 왼쪽 값 가져오기
            a = password.popleft()
            # i 값을 빼주기
            a -= i
            # a가 0이거나 0보다 작아지는 경우, 0으로 저장 후 종료
            if a <= 0:
                a = 0
                password.append(a)
                break
            # 아니면 그냥 추가
            else:
                password.append(a)

    result = []
    for j in range(len(password)):
        b = password.popleft()
        result.append(b)

    print(f'#{tc}', *result)