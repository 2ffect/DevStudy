# 피자 굽기
# 제한 시간 : 100
# 시작 시간 : 02/19 20:10
# 종료 시간 : 02/19 21:50

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

    # 녹여나갈 치즈 리스트와 유지할 피자 리스트
    cheese_list = []
    pizza_list = []
    # 피자의 상태
    pizza = 'bad'

    # 기본 화덕의 크기만큼 가져와서 추가하기
    for i in range(N):
        x = P.popleft()
        pizza_list.append(x)
        cheese_list.append(x)



    while True:
        # 피자를 녹이기, 치즈 리스트를 돌며 치즈를 녹이기
        # 치즈 리스트의 길이만큼 반복한다.
        L = len(cheese_list)
        for j in range(L):
            # 치즈가 0이 아닐 때,
            if cheese_list[j] != 0:
                # 치즈를 절반 녹인다.
                cheese_list[j] = cheese_list[j] // 2
                # 치즈를 녹였더니 0이 됐어, 그럼 새 피자를 추가해.
                # 근데, 남은 피자가 있을 때만
                if cheese_list[j] == 0:
                    if len(P) > 0:
                        new_pizza = P.popleft()
                        cheese_list.append(new_pizza)
                        pizza_list.append(new_pizza)
                        # 피자를 빼고 새로 넣었으면 녹여주기

                # 치즈 리스트 안에 하나의 치즈를 제외하고 모두 0 일 경우? pizza 를 good로 바꾸고 중단해.
                if cheese_list.count(0) == M-1:
                    pizza = 'good'
                    break


        # 피자가 good이면 while 탈출
        if pizza == 'good':
            break

    print(f'#{tc} {cheese_list.index(max(cheese_list))}')
