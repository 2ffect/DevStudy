# 빙고

# 시작 시간 : 02/28 16:20
# 종료 시간 : 02/28 17:30 까지~!

# 빙고판 가져오기 크기는 5*5 고정
bingo_board = [list(map(int, input().split())) for _ in range(5)]
# 5*5 로 주어지는 미션번호를 하나의 리스트로 인풋 받기
num_list = []
for _ in range(5):
    arr = list(map(int, input().split()))
    for z in range(5):
        num_list.append(arr[z])

# 사회자가 숫자를 부른 횟수
num_call = 0

# 미션 숫자 가져오기
# 해당 미션 숫자가 위치하는 빙고판 위치를 찾아서 번호를 지우기
# 번호를 지웠으면 빙고판에 빙고가 있는지 확인,
# - 어떻게 확인 할 것인가 ?

# 미션번호 하나 가져와서 빙고판 지우기
for num in num_list:
    # 번호를 불렀으니 횟수 + 1
    num_call += 1
    bingo = 0
    # 빙고판에서 번호 찾기
    for i in range(5):
        for j in range(5):
            # 맞으면 지우기
            if bingo_board[i][j] == num:
                bingo_board[i][j] = 0

    bingo_board_2 = list(zip(*bingo_board[::-1]))
    #행, 열, 각각 대각을 순회 하며 빙고 확인 총 빙고가 3이되면 중단

    for row in bingo_board:
        if row.count(0) == 5:
            bingo += 1
            if bingo == 3:
                break

    for row in bingo_board_2:
        if row.count(0) == 5:
            bingo += 1
            if bingo == 3:
                break

    cnt_1 = 0
    for k in range(5):
        for p in range(5):
            if k == p:
                if bingo_board[k][p] == 0:
                    cnt_1 += 1
    if cnt_1 == 5:
        bingo += 1

    cnt_2 = 0
    for q in range(5):
        for r in range(5):
            if q == r:
                if bingo_board_2[q][r] == 0:
                    cnt_2 += 1
    if cnt_2 == 5:
        bingo += 1

    if bingo >= 3:
        print(num_call)
        break
