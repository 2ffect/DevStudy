# 전봇대

# 시작 시간 : 03/08 13:45
# 종료 시간 : 03/08 13:57

import sys
sys.stdin = open('10580_input.txt')

T = int(input())

for tc in range(1, T+1):
    # 전선의 수
    N = int(input())

    # 전봇대 b (a는 필요없다.)
    b_post = [0] * 10001
    # 전선이 겹친 횟수
    cnt = 0
    for _ in range(N):
        # 전선의 위치 인풋 받기
        a, b = map(int, input().split())

        # a 부터 b 까지 전봇대에 1 로 전선의 영역을 표시
        for i in range(a, b+1):
            b_post[i] += 1

        else:
            # 숫자가 2가 된다면 겹친 것 모든 범위가 2라면 겹친 횟수를 1만 올려주기
            for j in range(a, b+1):
                # 조회 했을때 2 이상이 아니라면 ? break
                if b_post[j] < 2:
                    break
                # 2 이상이면 2번 겹친것, cnt +1

            else:
                cnt += 1

    print(f'#{tc} {cnt}')