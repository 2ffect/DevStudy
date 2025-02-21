# 피자 굽기

# 시작 시간 : 02/19 20:10
# 종료 시간 : 02/19 21:50 실패

# 시작 시간 : 02/21 15:15
# 종료 시간 :

# 화덕의 수만큼 피자를 순서대로 넣고
# 한바퀴 돌 때마다 피자의 치즈량이 반으로 줄어든다
# 치즈가 0이 되면 화덕에서 제거하고, 새로운 피자를 추가할 수 있다.
# 화덕에 가장 마지막까지 남아있는 피자의 번호는?

from collections import deque
import sys
sys.stdin = open("5099_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    # N = 배열의 크기, M = 피자의 수
    N, M = map(int, input().split())
    # P = 피자 근데 이제 치즈를 곁들인
    P = deque(map(int, input().split()))

    # 화덕 - 용량은 m
    fire = deque()
    # 피자 번호를 기록
    num = 1

    # 화덕의 용량만큼 피자를 꺼내서 넣기
    for _ in range(N):
        p = P.popleft()
        fire.append([p, num])
        num += 1

    # 피자 굽기
    # 화덕 안에 남은 피자가 0이 될 때 까지
    while len(fire) != 1:
        # 피자랑 번호 꺼내기.
        pizza, idx = fire.popleft()
        # 치즈를 반으로 줄이기
        pizza = pizza // 2

        # 치즈가 다 녹았을 때
        if pizza == 0:
            # 추가적으로 넣을 수 있는 피자가 있다면 가져와서 넣기
            if len(P) > 0:
                p = P.popleft()
                fire.append([p, num])
                num += 1

        # 아니면 그대로 다시 넣기
        else:
            fire.append([pizza, idx])

    # 마지막 남은 피자의 번호 가져오기
    last_pizza, num = fire.popleft()

    print(f'#{tc} {num}')