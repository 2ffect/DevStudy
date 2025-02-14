# 점점 커지는 당근의 개수

# 1차 시도
# 시작 시간 : 02/14 19:40
# 종료 시간 : 02/14 20:40 실패

# 2차 시도
# 시작 시간 : 02/14 20:45
# 종료 시간 : 02/14 20:49 성공




import sys
sys.stdin = open("9367_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))

    max_cnt = 1

    new_cnt = 0
    cnt = 0
    for i in range(1, N):
        if carrots[i-1] < carrots[i]:
            cnt += 1
            if new_cnt < cnt:
                new_cnt = cnt
        else:
            if new_cnt < cnt:
                new_cnt = cnt
            cnt = 0

    result = max_cnt + new_cnt

    print(f'#{tc} {result}')