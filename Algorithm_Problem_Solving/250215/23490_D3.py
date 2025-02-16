# [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크
# 제한 시간 : 2 시간

# 1차 시도
# 시작 시간 : 02/15 16:00
# 종료 시간 : 02/15 18:00 실패

# 2차 시도
# 시작 시간 : 02/16 14:45
# 종료 시간 : 02/16 15:15 성공

import sys
sys.stdin = open("23490_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    worklist = [list(map(int, input().split())) for _ in range(N)]

    # 각 작업서의 종료시간이 빠른 순서로 정렬,
    # e 에 종료시간이 가장 빠른 작업서의 종료시간을 넣어 둔 뒤, 작업서들을 순회 하며 s에 시작시간을 넣기
    # s 가 e 보다 작으면 탈락, e 와 같거나 크면 해당 s를 e에 넣고 cnt를 +1 한 뒤 다시 그 뒤 부터 작업서를 순회
    # 최종 cnt는 오늘 하루 작업할 수 있는 최대 트럭의 대수가 된다.

    sort_worklist = sorted(worklist, key=lambda x : x[1])

    max_cnt = 0

    s = sort_worklist[0][0]
    e = sort_worklist[0][1]
    # 하나를 넣었으니 cnt 는 1
    cnt = 1

    # 비교할 작업서 가져오기 위한 j
    for j in range(N):
        # 현재 종료시간보다 다음 작업서의 시작시간이 같거나, 클 경우
        if e <= sort_worklist[j][0]:
            # 시작 시간은 다음 작업서의 시작 시간이 되고
            s = sort_worklist[j][0]
            # 종료 시간은 다음 작업서의 종료 시간이 된다.
            e = sort_worklist[j][1]
            # 작업서가 변경 되었으므로 작업 횟수가 1 증가
            cnt += 1

    # 기준 작업서로 나머지 작업서 비교를 마쳤을 때,
    # max_cnt보다 cnt가 클 경우, 더 많은 작업이 가능하기 때문에 최대값 교체
    if max_cnt < cnt:
        max_cnt = cnt

    print(f'#{tc} {max_cnt}')