# 상호의 배틀필드

T = int(input())

for tc in range(1, T+1):
    # map size H * W
    H, W = map(int, input().split())
    # field
    field = [list(input()) for _ in range(H)]
    # orders range
    N = int(input())
    # orders
    orders = input()

    # 탱크가 이동할 수 있기 때문에 델타 범위 지정
    # 명령 별 델타의 경로
    # R == 0, D == 1, L == 2, U == 3
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    # 전차의 좌표
    k = p = 0
    # 전차가 바라보는 방향
    dr = 0
    # 전차의 좌표 찾기
    for i in range(H):
        for j in range(W):
            # 전장에 전차가 있을 때
            if field[i][j] in '^v<>':
                # 좌표를 따로 저장하고
                k, p = i, j
                # 전차의 방향을 확인
                if field[i][j] == '>':
                    dr = 0
                elif field[i][j] == 'v':
                    dr = 1
                elif field[i][j] == '<':
                    dr = 2
                elif field[i][j] == '^':
                    dr = 3


    # 명령을 하나씩 가져오기
    for order in orders:

        # 발사라면, 바라보는 방향으로 끝까지 포탄 발사 벽을 만나거나 맵 끝까지
        if order == 'S':
            # dr이 수평일 경우
            if dr in [0, 2]:
                # 맵의 너비만큼 바라보는 방향으로 발사!!
                for c in range(W):
                    nj = p + dj[dr] * c
                    # 범위가 유효하면 발사
                    if (0 <= nj < W):
                        # 강철 벽이라면, 종료
                        if field[k][nj] == '#':
                            break
                        # 벽돌 벽이라면, 평지로 변경
                        elif field[k][nj] == '*':
                            field[k][nj] = '.'
                            break
            # dr이 수직일 경우
            elif dr in [1, 3]:
                # 맵의 높이만큼 바라보는 방향으로 발사!!
                for c in range(H):
                    ni = k + di[dr] * c
                    # 범위가 유효하면 발사
                    if (0 <= ni < H):
                        # 강철 벽이라면, 종료
                        if field[ni][p] == '#':
                            break
                        # 벽돌 벽이라면, 평지로 변경
                        elif field[ni][p] == '*':
                            field[ni][p] = '.'
                            break

        # R == 0, D == 1, L == 2, U == 3
        # 위로 이동이라면 전차의 방향을 변경하고 가능하다면 1칸 전진
        elif order == 'U':
            dr = 3
            ni = k + di[dr]
            nj = p + dj[dr]
            # 유효하고 평지일 때 만!!
            if (0 <= ni < H) and (0 <= nj < W) and field[ni][nj] == '.':
                # 이동 하기전에 원래 있던 곳을 평지로 바꿔주고,
                field[k][p] = '.'
                # 한 칸 이동하고
                k, p = ni, nj
                # 전차의 머리를 돌려주기
                field[k][p] = '^'
                continue
            # 아니라면, 전차의 머리만 돌려주기
            else:
                field[k][p] = '^'
                continue

        # 위로 이동이라면 전차의 방향을 변경하고 가능하다면 1칸 전진
        elif order == 'L':
            dr = 2
            ni = k + di[dr]
            nj = p + dj[dr]
            # 유효하고 평지일 때 만!!
            if (0 <= ni < H) and (0 <= nj < W) and field[ni][nj] == '.':
                # 이동 하기전에 원래 있던 곳을 평지로 바꿔주고,
                field[k][p] = '.'
                # 한 칸 이동하고
                k, p = ni, nj
                # 전차의 머리를 돌려주기
                field[k][p] = '<'
                continue
            # 아니라면, 전차의 머리만 돌려주기
            else:
                field[k][p] = '<'
                continue

        # 위로 이동이라면 전차의 방향을 변경하고 가능하다면 1칸 전진
        elif order == 'D':
            dr = 1
            ni = k + di[dr]
            nj = p + dj[dr]
            # 유효하고 평지일 때 만!!
            if (0 <= ni < H) and (0 <= nj < W) and field[ni][nj] == '.':
                # 이동 하기전에 원래 있던 곳을 평지로 바꿔주고,
                field[k][p] = '.'
                # 한 칸 이동하고
                k, p = ni, nj
                # 전차의 머리를 돌려주기
                field[k][p] = 'v'
                continue
            # 아니라면, 전차의 머리만 돌려주기
            else:
                field[k][p] = 'v'
                continue

        # 위로 이동이라면 전차의 방향을 변경하고 가능하다면 1칸 전진
        elif order == 'R':
            dr = 0
            ni = k + di[dr]
            nj = p + dj[dr]
            # 유효하고 평지일 때 만!!
            if (0 <= ni < H) and (0 <= nj < W) and field[ni][nj] == '.':
                # 이동 하기전에 원래 있던 곳을 평지로 바꿔주고,
                field[k][p] = '.'
                # 한 칸 이동하고
                k, p = ni, nj
                # 전차의 머리를 돌려주기
                field[k][p] = '>'
                continue
            # 아니라면, 전차의 머리만 돌려주기
            else:
                field[k][p] = '>'
                continue


    print(f'#{tc}', ''.join(field[0]))
    for i in range(1, H):
        print(''.join(field[i]))
