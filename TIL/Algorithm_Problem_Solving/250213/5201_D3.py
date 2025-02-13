# 5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반

# 1차 시도
# 시작 시간 : 17:00
# 종료 시간 : 17:30

import sys
sys.stdin = open("5201_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    # 컨테이너와 트럭 수
    ct, truck = map(int, input().split())
    # 컨테이너 무게
    ct_w = list(map(int, input().split()))
    # 트럭의 적재 량
    truck_t = list(map(int, input().split()))

    # 트럭과 컨테이너 무게를 내림 차순 솔트 한 뒤
    # 각 각 순회하며 비교하여 적재 가능하면 cnt 에 추가 다음으로 넘어가기
    ct_w.sort(reverse = True)
    truck_t.sort(reverse = True)

    print('c :', ct_w)
    print('t :', truck_t)

    cnt = 0
    ans = 1
    for c in ct_w:
        for t in truck_t:
            if c > t:
                break
            if t >= c:
                cnt += c
                ans = 0
                break
        if ans == 0:
            ans = 1
            break
    print(cnt)