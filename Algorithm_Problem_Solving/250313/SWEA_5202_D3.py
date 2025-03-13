# 화물 도크

import sys
sys.stdin = open('5202_input.txt')


T = int(input())

for tc in range(1, T+1):
    # 작업서 수
    N = int(input())
    # 작업 리스트
    work_list = [list(map(int, input().split())) for _ in range(N)]

    # 작업서를 종료시간 기준으로 솔팅
    work_list.sort(key = lambda x : (x[1], x[0]))

    # 최대 작업량
    max_work = 0

    # 기준작업서 - 종료시간이 가장 빠른 작업서
    start = work_list[0][0]
    end = work_list[0][1]
    # 작업수 하나를 넣었으니 작업량은 1
    work_cnt = 1

    # 비교할 작업서 가져오기 위한 j 기준 작업서
    for j in range(1, N):
        # 현재 종료시간보다 다음 작업서의 시작시간이 같거나, 클 경우
        if end <= work_list[j][0]:
            # 시작 시간은 다음 작업서의 시작 시간이 되고
            start = work_list[j][0]
            # 종료 시간은 다음 작업서의 종료 시간이 된다.
            end = work_list[j][1]
            # 작업서가 변경 되었으므로 작업량 1 증가
            work_cnt += 1

    # 기준 작업서로 나머지 작업서 비교를 마쳤을 때,
    # max_cnt보다 cnt가 클 경우, 더 많은 작업이 가능하기 때문에 최대값 교체
    max_work = max(max_work, work_cnt)

    print(f'#{tc} {max_work}')