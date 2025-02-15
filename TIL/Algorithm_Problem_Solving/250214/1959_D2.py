# 두 개의 숫자열

# 1차 시도
# 시작 시간 : 02/14 21:00
# 종료 시간 : 02/14 21:30 실패

# 2차 시도
# 시작 시간 : 02/15 09:30
# 종료 시간 : 02/15 10:30 성공

import sys
sys.stdin = open("1959_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_num = 0

    # M 이 N 보다 큰 경우 (tc 1)
    if M > N:
        for i in range(M-N+1):
            # A[i+j]와 B[j] 들의 곱셈 끝나면 num 비교 후 초기화화
            # 가장 큰 값을 max_num 으로 바꾸기
            num = 0
            for j in range(N):
                num += (B[i+j] * A[j])
            if max_num < num:
                max_num = num

    # N 이 M 보다 큰 경우 (tc 2)
    # A와 B를 반대로 순회하면 됨
    else:
        for k in range(N-M+1):
            num = 0
            for p in range(M):
                num += (A[k+p] * B[p])
            if max_num < num:
                max_num =num

    print(f'#{tc} {max_num}')