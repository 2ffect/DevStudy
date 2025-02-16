# Gravity 복습

# 1차 시도
# 시작 시간 : 02/16 18:40
# 종료 시간 : 02/16 18:46

import sys
sys.stdin = open("23147_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 상자의 층수를 순회
    # i 번째 상자 층 보다 낮은 층의 수를 카운팅,
    # 카운팅이 가장 높으면 갱신

    max_cnt = 0

    for i in range(N):
        cnt = 0
        for j in range(1, N-i):
            if arr[i] > arr[i+j]:
                cnt += 1

        max_cnt = max(max_cnt, cnt)

    print(f'#{tc} {max_cnt}')