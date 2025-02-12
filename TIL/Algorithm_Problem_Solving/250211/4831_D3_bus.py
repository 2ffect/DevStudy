import sys
sys.stdin = open("4831_input.txt", "r")

# 전기버스
T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    # 정류장 별 충전기 설치여부 0 - 미설치 / 1 - 설치
    charge_site = [0] * (N+1)
    for c in charge:
        charge_site[c] += 1

    # 충전 횟수
    cnt = 0
    # 출발점
    i = 0

    # N+1 만큼 순회한다(버스정류장 버스가 이동)
    # 근데 한 번 이동거리는 i + K 만큼 가능하다.
    # i + K 가 N을 넘어서면 순회를 종료한다.
    while i + K < N:
        # i 가 0 일 때, i + K 까지 갈 수 있다.
        # i 가 i + K 까지 가는동안 충전기가 있는지 봐야한다.
        # charge_site[i] ~ charge_site[1+K] 동안 가장 멀리 있는 충전기.
        # 구간 내 가장 멀리있는(인덱스가 가장 큰) 충전기 까지 간다.
        # 거기서 다시 출발해야 하니까, i 는 충전기가 있을 때 가장 멀리있는 j (가장 큰 j)
        # 가장 멀리 있는 충전기 찾으면 cnt +1

        # 가장 멀리 있는 j == 1을 찾기위해 거꾸로 순회
        for j in range(i+K, i, -1):
            # j 가 1 일 때 즉, 가장 멀리 있는 충전기가 있을 때
            if charge_site[j] == 1:
                # i 는 j 로 바꾼다. j는 i가 다시 출발해야하는 위치
                i = j
                # 충전횟수 + 1
                cnt += 1
                # 더 이상 충전 필요없으니까 break 로 for문 탈출 새로운 위치에서 for문 진입 (while 조건 내에서 계속 수행)
                break

        # cnt 가 0 이면 == 이동한 구간 내에서 발견된 충전기가 없으면,
        # 순회 할 필요가 없다.
        else:
            cnt = 0
            break

    print(f'#{tc} {cnt}')