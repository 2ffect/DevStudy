import sys
sys.stdin = open("C:/Users/SSAFY/Desktop/JH/sample_input.txt", "r")

for tc in range(1, 11):
    N = int(input())
    n_high = list(map(int, input().split()))
    # 뷰가 좋은 집
    view = 0

    for i in range(2, N - 2):
        # 기준이 가장 높은지 확인
        height = n_high[i]
        p_list = []
        # 기준 건물이 첫 번째로 큰 건물이 맞을 때 걔 빼고 리스트에 넣기
        for j in range(i - 2, i + 3):
            if n_high[j] > height:
                height = n_high[j]
            if i != j:
                p_list.append(n_high[j])

        # print(p_list, height)

        # 두번째로 높은 건물 찾기
        if p_list:
            new_high = p_list[0]
            for new in p_list:
                if new > new_high:
                    new_high = new

        # print(height, new_high)
        # height 랑 기준건물이랑 같을 때 view 추가
        # 같지 않으면 무수히 많은 0이 같이 더해짐
            if height == n_high[i]:
                # print(height, new_high)
                view += height - new_high

    print(f'#{tc} {view}')