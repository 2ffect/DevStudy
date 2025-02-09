import sys
sys.stdin = open("23147.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 가장 큰 낙차 설정
    max_cnt = 0
    for i in range(N):
        point = arr[i]

        # point 보다 낮은 건물의 수 = point의 낙차
        cnt = 0
        for j in range(i + 1, N):
            # point 우측 건물 하나씩 순회
            vs_point = arr[j]
            # point 보다 낮으면 cnt +1
            if vs_point < point:
                cnt += 1

        # 가장 큰 낙차일 경우 갱신
        if max_cnt < cnt:
            max_cnt = cnt

    print(f'#{tc} {max_cnt}')