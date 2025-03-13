# 컨테이너 운반

import sys
sys.stdin = open('5201_input.txt')

T = int(input())

for tc in range(1, T+1):
    # N = 컨테이너 수 / M = 트럭 수
    N, M = map(int, input().split())
    # 컨테이너 리스트
    C = list(map(int, input().split()))
    # 트럭 리스트
    T = list(map(int, input().split()))
    # 트럭이 컨테이너보다 크거나 같으면 옮길 수 있다.
    # 정렬을 하고 하나씩 비교해서 컨테이너 무게를 추가한다.
    C.sort(reverse=True)
    T.sort(reverse=True)

    # 총 이동 무게
    total_w = 0
    # i는 항상 0으로 고정 - 맨 앞 값만 비교
    i = 0
    # 최대 비교횟수 ( N, M 중 더 큰 수)
    max_try = max(N, M)

    for _ in range(max_try):
        # 컨테이너나, 트럭이 남아 있을 때 비교한다.
        if len(C) > 0 and len(T) > 0:
            # 트럭의 적재량이 컨테이너의 무게보다 넉넉하거나 같을 경우 탑재가능
            if T[i] >= C[i]:
                # 탑재를 한다 == 이동 가능 (컨테이너 무게 추가)
                total_w += C[i]
                # 이동을 했으니 트럭과 컨테이너를 리스트에서 제거
                T.pop(i), C.pop(i)
            # 트럭의 적재량보다 컨테이너의 무게가 더 클경우, 해당 컨테이너는 비교대상에서 제외
            # 다음 컨테이너를 비교해야한다. 더 작은 컨테이너가 나올 수 있음
            else:
                C.pop(i)

    print(f'#{tc} {total_w}')