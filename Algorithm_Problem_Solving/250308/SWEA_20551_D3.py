# 증가하는 사탕 수열

# 시작 시간 : 03/08 13:15
# 종료 시간 : 03/08

import sys
sys.stdin = open('20551_input.txt')

T = int(input())
for tc in range(1, T+1):
    a, b, c = map(int, input().split())

    # 먹은 사탕 수
    eat_candy = 0

    if (a >= 1) and (b >= 2) and (c >= 3):
        while a >= b:
            a -= 1
            eat_candy += 1
            continue
        while b >= c:
            b -= 1
            eat_candy += 1
            if a >= b:
                a -= 1
                eat_candy += 1
            continue

    else:
        eat_candy = -1


    print(f'#{tc} {eat_candy}')