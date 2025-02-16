# View 복습

# 1차 시도
# 시작 시간 : 02/16 18:00
# 종료 시간 : 02/16 18:32 성공

import sys
sys.stdin = open("1206_input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    # 5개의 건물을 가져와서 가운데가 가장 높은지 확인.
    # 맞다면 두 번째로 높은 건물을 빼주기 (조망권 세대)
    total_view = 0


    for i in range(2, N-2):
        point = arr[i]
        n_list = []
        for j in range(i-2, i+3):
            # point가 가장 큰 건물 일때
            if arr[i] > point:
                point = arr[i]
            # point 빼고 리스트에 담기
            if i != j:
                n_list.append(arr[j])

        # 두 번째로 높은 건물 찾기
        # 가장 높은 층 과 빼기
        result = point - max(n_list)

        # 뺀 값이 0 보다 클 때 뷰에 더해주기
        if result > 0:
            total_view += result



    print(f'#{tc} {total_view}')