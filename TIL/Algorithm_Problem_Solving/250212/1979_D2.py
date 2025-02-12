# 어디에 단어가 들어갈 수 있을까
# 1차 시도
# 시작 시간 : 2/12 20:50
# 종료 시간 : 2/12 21:27

import sys
sys.stdin = open("1979_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = [list(map(str, input().split())) for _ in range(n)]

    k_list = []

    # 행을 하나의 문자열로 바꿔서 가져오기
    for i in arr:
        row = ''.join(i)
        # 변환한 행을 순회하며 1이 연속되는 횟수
        # 연속 된 1의 수
        cnt = 0
        for j in row:
            # 연속 되게 1이 나온다면 cnt가 1씩 증가
            if j == "1":
                cnt += 1
            # 0 이 나오면 cnt를 0으로 초기화
            # 그 전에 cnt 가 k 라면 리스트에 추
            else:
                if cnt == k:
                    k_list.append(cnt)
                cnt = 0
        if cnt == k:
            k_list.append(cnt)

    # 배열 시계 방향으로 90도 뒤집기 (행 열 위치 바꾸기)
    arr_2 = zip(*arr[::-1])

    # 행을 하나의 문자열로 바꿔서 가져오기
    for i in arr_2:
        row = ''.join(i)
        cnt = 0
        for j in row:
            if j == "1":
                cnt += 1
            else:
                if cnt == k:
                    k_list.append(cnt)
                cnt = 0
        if cnt == k:
            k_list.append(cnt)
    result = len(k_list)

    print(f'#{tc} {result}')