# 간단한 소인수분해
# 제한 시간 1시간

# 시작 시간 : 02/18 18:40
# 종료 시간 : 02/18 18:51 성공

import sys
sys.stdin = open("1945_input.txt", "r")

T = int(input())

# 소인수분해에 사용 될 리스트
num = [2, 3, 5, 7, 11]
N = len(num)

for tc in range(1, T+1):
    M = int(input())

    # 받아온 정수 M 을 num을 활용해서 소인수 분해 한 뒤
    # 각 num 별로 사용 된 횟수를 출력,
    # num을 사용 할 때 마다 cnt를 증가시키고, 리스트에 추가하기.

    cnt_list = []
    for i in range(N):
        # num[i]로 M을 더 이상 나눌 수 없을 때 까지 나누기.
        cnt = 0
        while True:
            if M % num[i] == 0:
                M = M // num[i]
                cnt += 1
            # 나누어 떨어지지 않으면 cnt 를 cnt_list에 추가하고 while문 이탈
            else:
                cnt_list.append(cnt)
                break

    print(f'#{tc}', *cnt_list)