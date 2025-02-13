# 스도쿠 검증
# 1차 시도
# 시작 시간 : 02/13 14:20
# 종료 시간 : 02/13 15:20 실패

# 2차 시도 - 코드 리셋
# 시작 시간 : 02/13 16:05
# 종료 시간 : 02/13 16:28


import sys
sys.stdin = open("1974_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = 9
    arr = [list(map(int, input().split())) for _ in range(N)]


    # 스도쿠 조건에 맞는 리스트
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 모든 스도쿠가 참이라는 가정
    result = 1
    for _ in range(N):
        # 행을 하나씩 가져와 정렬을 통해 조건에 맞는지 확인
        for i in range(N):
            # 행을 담을 리스트
            row_list = []
            for j in range(N):
                # 담기
                row_list.append(arr[i][j])
            # 담은 후 정렬
            row_list.sort()
            # 정렬 후 조건과 같은지 확인하여 다를경우, 해당 퍼즐은 스도쿠가 아님
            # result를 0으로 바꾸고 행 비교를 멈춤
            if row_list != num:
                result = 0
                break

        # 스도쿠가 아니기 때문에 해당 tc는 더이상 순회 할 필요가 없음
        # 결과를 출력 후 tc를 탈출
        if result == 0:
            print(f'#{tc} {result}')
            break

        # 행 순회 후 모두가 참이라면, 열 순회를 시작
        # 열 순회는 행을 시계방향으로 90도 돌려 열을 행의 위치에 두고 순회
        arr2 = list(zip(*arr[::-1]))

        for i in range(N):
            # 담을 리스트
            col_list = []
            for j in range(N):
                # 담기
                col_list.append(arr2[i][j])
            # 담은 후 정렬
            col_list.sort()
            # 정렬 후 조건과 같은지 확인하여 다를경우, 해당 퍼즐은 스도쿠가 아님
            # result를 0으로 바꾸고 행 비교를 멈춤
            if col_list != num:
                result = 0
                break
        # 스도쿠가 아니기 때문에 해당 tc는 더이상 순회 할 필요가 없음
        # 결과를 출력 후 tc를 탈출
        if result == 0:
            print(f'#{tc} {result}')
            break


        # 행과 열이 모두 스도쿠 조건에 맞다면 3*3 탐색하기
        # 3*3의 가운데 지점을 지정 후 델타 탐색으로 본인 포함 9군데를 list에 추가
        # list 정렬 후 num과 비교하여 flag 수정.
        # 모든 탐색 뒤 flag true 라면 1, Fasle 라면 0 출력

        # 퍼즐 전체를 순회하며 3*3 구간을 확인 리스트 만들고 num과 비교
        # 3*3 씩 볼거니까 기준점은 3칸씩만 이동
        for i in range(0, N, 3):
            for j in range(0, N, 3):
                # 각 포인트 점에서 3*3 순회
                list_3 = []
                for k in range(3):
                    for p in range(3):
                        list_3.append(arr[k+i][j+p])
                list_3.sort()
                if list_3 != num:
                    result = 0
                    break

            if result == 0:
                break

        if result == 0:
            print(f'#{tc} {result}')
            break

    if result != 0:
        print(f'#{tc} {result}')